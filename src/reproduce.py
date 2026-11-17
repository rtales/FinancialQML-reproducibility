#!/usr/bin/env python3
"""Recompute the published FinancialQML descriptive results from frozen inputs."""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.metadata
import json
import os
import platform
import sys
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DEFAULT_OUT = ROOT / "outputs" / "reproduced"
FROZEN_INPUTS = DATA / "frozen_analysis_inputs.zip"
FROZEN_INPUTS_SHA256 = "b9323340a87e16788be06ed432187bf326808e3f8dbc384855b2c19ed4dee728"
INPUT_MANIFEST_SHA256 = "4334ff5d76f1281cafeaa1b82f0994f992ef1142d4b8b7e58f6c585a38017368"

FUNNEL_PATHS = {
    "macro_target_alignment": {"claim_target"},
    "core_claim_design_alignment": {
        "claim_target",
        "claim_target_detail",
        "result_basis",
        "task_context.evaluation_design",
    },
    "method_metric_alignment": {
        "claim_target",
        "claim_target_detail",
        "result_basis",
        "task_context.evaluation_design",
        "cost_scope",
        "subject_method.computational_model",
        "metric.unit",
    },
}

TABLE6_FIELDS = (
    ("metric.definition_ref", "Metric definition reference"),
    ("subject_method.algorithm_id", "Algorithm identifier"),
    ("metric.metric_id", "Metric identifier"),
    ("metric.unit", "Metric unit"),
    ("subject_method.implementation_protocol_id", "Implementation protocol ID"),
    ("scale.n_assets", "Number of assets"),
    ("claim_target_detail", "Claim-target detail"),
    ("claim_target", "Claim target"),
    ("result_basis", "Result basis"),
    ("task_context.evaluation_design", "Evaluation design"),
    ("comparator.protocol_id", "Comparator protocol ID"),
    ("comparator.method_id", "Comparator method ID"),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def archive_member(archive: zipfile.ZipFile, path: str) -> Any:
    return json.loads(archive.read(path))


def verify_archive() -> None:
    input_manifest_path = DATA / "input_manifest.json"
    if sha256(input_manifest_path) != INPUT_MANIFEST_SHA256:
        raise ValueError("input manifest checksum mismatch")
    input_manifest = json.loads(input_manifest_path.read_text(encoding="utf-8"))
    for item in input_manifest["files"]:
        path = DATA / item["path"]
        if not path.is_file() or path.stat().st_size != item["bytes"]:
            raise ValueError(f"input missing or size mismatch: {item['path']}")
        if sha256(path) != item["sha256"]:
            raise ValueError(f"input checksum mismatch: {item['path']}")
    article_manifest = json.loads((DATA / "article-manifest.json").read_text(encoding="utf-8"))
    manuscript_sha = sha256(DATA / "FinancialQML_EPJQT.md")
    if manuscript_sha != article_manifest["manuscript_sha256"]:
        raise ValueError("article source does not match its frozen manifest")

    actual = sha256(FROZEN_INPUTS)
    if actual != FROZEN_INPUTS_SHA256:
        raise ValueError(f"frozen analysis input hash mismatch: {actual}")
    with zipfile.ZipFile(FROZEN_INPUTS) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise ValueError(f"corrupt ZIP member: {bad}")
        manifest = json.loads(archive.read("FROZEN_INPUTS_MANIFEST.json"))
        for item in manifest["files"]:
            member = item["path"]
            payload = archive.read(member)
            actual_member = hashlib.sha256(payload).hexdigest()
            if actual_member != item["sha256"]:
                raise ValueError(f"manifest hash mismatch: {member}")
            if len(payload) != item["bytes"]:
                raise ValueError(f"manifest size mismatch: {member}")
        expected_members = {item["path"] for item in manifest["files"]}
        expected_members.add("FROZEN_INPUTS_MANIFEST.json")
        if set(archive.namelist()) != expected_members:
            raise ValueError("frozen input ZIP contains unmanifested or missing members")


def split_paths(value: object) -> set[str]:
    return {part for part in str(value or "").split(";") if part}


def expected_paths(profile: dict[str, Any]) -> set[str]:
    """Apply the frozen L0 target-specific applicability rules to a public profile."""
    common = {
        "finance_context.application",
        "claim_target",
        "subject_method.algorithm_id",
        "subject_method.computational_model",
        "task_context.evaluation_design",
        "metric.metric_id",
        "metric.definition_ref",
        "metric.unit",
        "result_basis",
    }
    missing = split_paths(profile.get("missing_required_paths"))
    if profile.get("claim_target_detail"):
        common.add("claim_target_detail")
    comparator_values = (
        profile.get("comparator_surface"),
        profile.get("comparator_method_id"),
        profile.get("comparator_protocol_id"),
    )
    comparative_direction = profile.get("direction") in {
        "outperforms",
        "underperforms",
        "no_difference",
    }
    comparator_present = any(comparator_values) or bool(
        missing & {"comparator.method_id", "comparator.protocol_id"}
    )
    if comparative_direction and comparator_present:
        common.update({"comparator.method_id", "comparator.protocol_id"})

    target = profile["claim_target"]
    if target == "economic_performance":
        common.update(
            {
                "finance_context.universe_id",
                "finance_context.universe_as_of",
                "finance_context.objective_id",
                "finance_context.constraints_id",
                "finance_context.temporal_protocol.split_policy",
                "finance_context.temporal_protocol.horizon",
                "finance_context.rebalance_frequency",
                "finance_context.transaction_cost_model_id",
                "finance_context.temporal_protocol.evaluation_start",
                "finance_context.temporal_protocol.evaluation_end",
            }
        )
    elif target == "solution_quality":
        common.update(
            {
                "task_context.instance_generator",
                "finance_context.objective_id",
                "finance_context.constraints_id",
                "scale.n_assets",
                "subject_method.implementation_protocol_id",
            }
        )
    elif target == "pricing_accuracy":
        common.update(
            {
                "finance_context.contract_family",
                "finance_context.exercise_style",
                "finance_context.payoff_id",
                "finance_context.underlying_id",
                "finance_context.pricing_measure",
                "finance_context.dynamics_model_id",
                "finance_context.calibration_id",
                "finance_context.maturity",
                "finance_context.moneyness",
                "finance_context.discretization_id",
                "finance_context.target_error",
            }
        )
    elif target in {"computational_cost", "resource_requirement", "feasibility"}:
        common.update(
            {
                "cost_scope",
                "scale.n_assets",
                "subject_method.implementation_protocol_id",
            }
        )
    else:
        raise ValueError(f"unsupported L0 claim target: {target}")

    # The release omits source-local values, but its frozen profile records every
    # required path whose value was missing. These paths are also applicability evidence.
    common.update(missing)
    return common


def compute_table6(
    profiles: list[dict[str, Any]],
    pairs: list[dict[str, Any]],
    claim_uid: dict[str, str],
    l0_diagnostics: dict[tuple[str, str], dict[str, Any]],
) -> list[dict[str, Any]]:
    profile_by_id = {row["claim_id"]: row for row in profiles}
    paths_by_id = {row["claim_id"]: expected_paths(row) for row in profiles}
    rows: list[dict[str, Any]] = []
    for path, label in TABLE6_FIELDS:
        applicable = missing = different = 0
        for pair in pairs:
            left_id, right_id = pair["left_claim_id"], pair["right_claim_id"]
            if claim_uid[left_id] == claim_uid[right_id]:
                continue
            left, right = profile_by_id[left_id], profile_by_id[right_id]
            required = paths_by_id[left_id] | paths_by_id[right_id]
            if path not in required:
                continue
            applicable += 1
            diagnostic = l0_diagnostics[tuple(sorted((left_id, right_id)))]
            if path in set(diagnostic["missing"]):
                missing += 1
            elif path in set(diagnostic["mismatched"]):
                different += 1
        blocked = missing + different
        rows.append(
            {
                "field": path,
                "label": label,
                "applicable_pairs": applicable,
                "missing_pairs": missing,
                "different_present_value_pairs": different,
                "blocked_pairs": blocked,
                "unblocked_applicable_pairs": applicable - blocked,
            }
        )
    return rows


def compute_results() -> dict[str, Any]:
    verify_archive()
    with zipfile.ZipFile(FROZEN_INPUTS) as archive:
        contract_pairs = archive_member(archive, "contract_pairs.json")["pairs"]
        field_ablation = archive_member(archive, "field_ablation_results.json")
        identifier_ablation = json.loads(
            (DATA / "identifier-ablation-results.json").read_text(encoding="utf-8")
        )
        ba_summary_reference = json.loads(
            (DATA / "ba-summary.json").read_text(encoding="utf-8")
        )
    profiles = json.loads((DATA / "article-profiles.json").read_text(encoding="utf-8"))
    pairs = json.loads((DATA / "article-pair-diagnostics.json").read_text(encoding="utf-8"))
    claim_paper_map = json.loads((DATA / "claim-paper-map.json").read_text(encoding="utf-8"))

    ba_rows = list(csv.DictReader((DATA / "ba-scores.tsv").open(encoding="utf-8"), delimiter="\t"))
    ba_by_family: dict[str, list[float]] = {}
    ba_equal_scores = []
    for row in ba_rows:
        ba_by_family.setdefault(row["family"], []).append(
            float(row["applicable_benchmark_assessability_score"])
        )
        ba_equal_scores.append(float(row["equal_weight_applicable_score"]))
    weighted_ba = {
        "all": round(sum(value for values in ba_by_family.values() for value in values) / len(ba_rows), 4),
        **{
            family: round(sum(values) / len(values), 4)
            for family, values in sorted(ba_by_family.items())
        },
    }
    equal_weight_ba = round(sum(ba_equal_scores) / len(ba_equal_scores), 4)
    ba_expected = {
        ("all" if item["group_type"] == "all" else item["group_value"]): item["mean_score"]
        for item in ba_summary_reference
        if item["group_type"] in {"all", "family"}
    }
    if weighted_ba != ba_expected or equal_weight_ba != 0.8274:
        raise ValueError(
            f"benchmark-assessability results differ from frozen values: "
            f"{weighted_ba}, equal-weight={equal_weight_ba}"
        )

    claim_uid = {row["claim_id"]: row["paper_uid"] for row in claim_paper_map}
    if len(claim_uid) != len(claim_paper_map) or set(claim_uid) != {
        row["claim_id"] for row in profiles
    }:
        raise ValueError("claim IDs in the paper map and article profiles differ")
    if {row["family"] for row in claim_paper_map} != {row["family"] for row in profiles}:
        raise ValueError("claim families in the paper map and article profiles differ")
    papers_by_uid: dict[str, set[str]] = {}
    for row in claim_paper_map:
        papers_by_uid.setdefault(row["paper_uid"], set()).add(row["family"])
    if any(len(families) != 1 for families in papers_by_uid.values()):
        raise ValueError("a paper identifier is assigned to multiple study families")
    paper_family_counts = Counter(next(iter(families)) for families in papers_by_uid.values())
    identifier_ablation_results = compute_identifier_ablation(
        contract_pairs, profiles, identifier_ablation
    )

    cross_pairs = [
        pair
        for pair in pairs
        if claim_uid[pair["left_claim_id"]] != claim_uid[pair["right_claim_id"]]
    ]
    if len(papers_by_uid) != 56 or len(profiles) != 240 or len(cross_pairs) != 13873:
        raise ValueError("frozen corpus dimensions do not match the submitted study")

    dimensions: dict[str, dict[str, int]] = {}
    for key in (
        "family",
        "claim_target",
        "result_basis",
        "evaluation_design",
        "computational_model",
        "market_region",
    ):
        counts = Counter(str(row.get(key) or "Missing/blank") for row in profiles)
        dimensions[key] = dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))

    missing_counts: Counter[str] = Counter(
        path for row in profiles for path in split_paths(row.get("missing_required_paths"))
    )
    table4_paths = [
        "subject_method.algorithm_id",
        "metric.metric_id",
        "metric.definition_ref",
        "subject_method.implementation_protocol_id",
        "metric.unit",
        "comparator.protocol_id",
        "comparator.method_id",
        "scale.n_assets",
        "finance_context.objective_id",
        "finance_context.constraints_id",
    ]
    missing_by_claim = {path: missing_counts[path] for path in table4_paths}

    funnel = []
    paper_survivors = []
    for tier in ("family_topic_pool", *FUNNEL_PATHS, "strict_direct_effect"):
        block = FUNNEL_PATHS.get(tier, set())
        selected = [
            row
            for row in cross_pairs
            if (
                row["verdict"] == "comparable"
                if tier == "strict_direct_effect"
                else not (split_paths(row.get("reasons")) & block)
            )
        ]
        paper_pairs = {
            tuple(sorted((claim_uid[row["left_claim_id"]], claim_uid[row["right_claim_id"]])))
            for row in selected
        }
        funnel.append(
            {
                "tier": tier,
                "claim_pairs": len(selected),
                "F1_claim_pairs": sum(row["family"] == "F1" for row in selected),
                "F2_claim_pairs": sum(row["family"] == "F2" for row in selected),
                "paper_pairs": len(paper_pairs),
                "share_of_universe": len(selected) / len(cross_pairs),
            }
        )
        paper_survivors.append(len(paper_pairs))

    l0_diagnostics = {
        tuple(sorted((row["left_claim_id"], row["right_claim_id"]))): {
            "missing": row["missing_paths"],
            "mismatched": row["mismatched_paths"],
        }
        for row in cross_pairs
    }
    table6 = compute_table6(profiles, pairs, claim_uid, l0_diagnostics)
    # Cross-check pair-derived applicable-field decompositions against the
    # separately frozen summary included with this release.
    expected = json.loads((DATA / "finance-v9-applicability-summary.json").read_text())
    expected_fields = {row["field"]: row for row in expected["fields"]}
    for row in table6:
        reference = expected_fields[row["field"]]
        for key in (
            "applicable_pairs",
            "missing_pairs",
            "different_present_value_pairs",
            "blocked_pairs",
            "unblocked_applicable_pairs",
        ):
            if row[key] != reference[key]:
                raise ValueError(
                    f"table 6 audit mismatch for {row['field']} {key}: "
                    f"{row[key]} != {reference[key]}"
                )

    transitions = contract_transition_counts(contract_pairs)
    field_ablation_results = compute_field_ablation(contract_pairs, field_ablation)
    return {
        "schema_version": "financialqml-public-reproduction-v1",
        "frozen_analysis_inputs_sha256": FROZEN_INPUTS_SHA256,
        "corpus": {
            "papers": len(papers_by_uid),
            "claims": len(profiles),
            "quote_verified_claims": sum(bool(row["quote_verified"]) for row in profiles),
            "papers_by_family": dict(paper_family_counts),
            "claims_by_family": dict(Counter(str(row["family"]) for row in profiles)),
            "cross_paper_claim_pairs": len(cross_pairs),
        },
        "table_3_claim_dimensions": dimensions,
        "table_4_missing_claim_values": missing_by_claim,
        "table_5_evidence_alignment_funnel": funnel,
        "table_5_paper_pair_survival": paper_survivors,
        "table_6_blockers": table6,
        "contract_verdicts_and_transitions": transitions,
        "field_ablation_verdicts": field_ablation["observed_verdicts"],
        "field_ablation_by_path": field_ablation_results,
        "identifier_ablation": {
            "n_pairs": identifier_ablation["n_pairs"],
            "same_macro_target_n": identifier_ablation["same_macro_target_n"],
            "policies": identifier_ablation_results,
        },
        "benchmark_assessability": {
            "weighted_mean": weighted_ba,
            "equal_weight_mean": equal_weight_ba,
        },
    }


def contract_transition_counts(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_contract: dict[str, dict[tuple[str, str], str]] = {}
    for row in rows:
        if row.get("scenario") != "full_original":
            continue
        contract = str(row["contract"])
        by_contract.setdefault(contract, {})[(row["left"], row["right"])] = str(row["verdict"])
    expected_contracts = {"L0", "T1", "I1"}
    if set(by_contract) != expected_contracts:
        raise ValueError(f"unexpected contract set: {sorted(by_contract)}")
    counts = {}
    for contract, pairs in by_contract.items():
        distribution = Counter(pairs.values())
        counts[contract] = {
            verdict: distribution.get(verdict, 0)
            for verdict in ("comparable", "insufficient_information", "incomparable")
        }
    transitions = {}
    matrices = {}
    for a, b in (("L0", "T1"), ("L0", "I1"), ("T1", "I1")):
        left, right = by_contract[a], by_contract[b]
        if left.keys() != right.keys():
            raise ValueError(f"contract pair populations differ: {a} vs {b}")
        transitions[f"{a}_to_{b}"] = sum(left[key] != right[key] for key in left)
        matrix: dict[str, dict[str, int]] = {}
        for key in left:
            matrix.setdefault(left[key], {}).setdefault(right[key], 0)
            matrix[left[key]][right[key]] += 1
        matrices[f"{a}_to_{b}"] = matrix
    return {
        "verdict_counts": counts,
        "changed_pair_counts": transitions,
        "transition_matrices": matrices,
    }


def compute_identifier_ablation(
    rows: list[dict[str, Any]],
    profiles: list[dict[str, Any]],
    frozen_result: dict[str, Any],
) -> dict[str, Any]:
    profile_by_id = {row["claim_id"]: row for row in profiles}
    policy_by_name = frozen_result["policies"]
    results: dict[str, Any] = {}
    for policy_name, policy in policy_by_name.items():
        omitted = set(policy["omitted_paths"])
        outcomes = {
            "all_pairs": Counter(),
            "same_macro_target": Counter(),
        }
        for row in rows:
            if row.get("scenario") != "full_original" or row.get("contract") != "L0":
                continue
            missing = set(row["missing"]) - omitted
            mismatched = set(row["mismatched"]) - omitted
            outcome = (
                "incomparable"
                if mismatched
                else "insufficient_information"
                if missing
                else "counterfactual_blocker_free"
            )
            outcomes["all_pairs"][outcome] += 1
            left, right = profile_by_id[row["left"]], profile_by_id[row["right"]]
            if left["claim_target"] == right["claim_target"]:
                outcomes["same_macro_target"][outcome] += 1

        population_results = {}
        for population, counter in outcomes.items():
            expected_population = policy["population_results"][population]
            computed = {
                outcome: counter.get(outcome, 0)
                for outcome in (
                    "counterfactual_blocker_free",
                    "incomparable",
                    "insufficient_information",
                )
            }
            if sum(counter.values()) != expected_population["n_pairs"]:
                raise ValueError(f"identifier sensitivity pair population differs: {policy_name}/{population}")
            if computed != expected_population["outcomes"]:
                raise ValueError(f"identifier sensitivity results differ: {policy_name}/{population}")
            population_results[population] = {
                "n_pairs": sum(counter.values()),
                "outcomes": computed,
            }
        results[policy_name] = {
            "omitted_paths": sorted(omitted),
            "population_results": population_results,
        }
    return results


def compute_field_ablation(
    rows: list[dict[str, Any]], frozen_result: dict[str, Any]
) -> list[dict[str, Any]]:
    selected = [
        row for row in rows
        if row.get("scenario") == "full_original" and row.get("contract") == "L0"
    ]
    if len(selected) != frozen_result["n_pairs"]:
        raise ValueError("field-ablation pair denominator differs")
    observed = Counter(row["verdict"] for row in selected)
    normalized = {
        verdict: observed.get(verdict, 0)
        for verdict in ("comparable", "incomparable", "insufficient_information")
    }
    if normalized != frozen_result["observed_verdicts"]:
        raise ValueError("field-ablation baseline verdicts differ")
    for row in selected:
        blockers, missing, mismatched = map(
            set, (row["blockers"], row["missing"], row["mismatched"])
        )
        if blockers != missing | mismatched or missing & mismatched:
            raise ValueError("stored field-ablation blocker partition is inconsistent")
        expected = (
            "incomparable" if mismatched
            else "insufficient_information" if missing
            else "comparable"
        )
        if row["verdict"] != expected:
            raise ValueError("stored L0 verdict differs from blocker partition")

    fields = sorted({path for row in selected for path in row["blockers"]})
    results = []
    for field in fields:
        counts = Counter()
        affected = 0
        for row in selected:
            blockers = set(row["blockers"])
            if field not in blockers:
                continue
            affected += 1
            remaining = blockers - {field}
            if not remaining:
                outcome = "counterfactual_comparable"
            elif remaining & set(row["mismatched"]):
                outcome = "remaining_incomparable"
            else:
                outcome = "remaining_insufficient_information"
            counts[outcome] += 1
        result = {
            "field": field,
            "pairs_affected": affected,
            "counterfactual_comparable": counts["counterfactual_comparable"],
            "remaining_incomparable": counts["remaining_incomparable"],
            "remaining_insufficient_information": counts["remaining_insufficient_information"],
        }
        partition = sum(
            result[key]
            for key in (
                "counterfactual_comparable",
                "remaining_incomparable",
                "remaining_insufficient_information",
            )
        )
        if partition != affected:
            raise ValueError(f"field-ablation outcome partition failed: {field}")
        results.append(result)
    if results != frozen_result["results"]:
        raise ValueError("one-field-ablation output differs from the frozen result")
    return results


def write_tsv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def generate_figures(results: dict[str, Any], out_dir: Path) -> None:
    mpl_cache = out_dir / ".matplotlib"
    mpl_cache.mkdir(parents=True, exist_ok=True)
    xdg_cache = mpl_cache / "xdg"
    xdg_cache.mkdir(parents=True, exist_ok=True)
    # Use an output-local cache so a clean run does not depend on a user's
    # home-directory font cache or machine-level write permissions.
    os.environ["MPLCONFIGDIR"] = str(mpl_cache)
    os.environ["XDG_CACHE_HOME"] = str(xdg_cache)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    ba_rows = list(
        csv.DictReader((DATA / "ba-scores.tsv").open(encoding="utf-8"), delimiter="\t")
    )
    ba_by_family: dict[str, list[float]] = {}
    for row in ba_rows:
        ba_by_family.setdefault(row["family"], []).append(
            float(row["applicable_benchmark_assessability_score"])
        )
    figure_dir = out_dir / "figures"
    figure_dir.mkdir(parents=True, exist_ok=True)
    funnel = results["table_5_evidence_alignment_funnel"]
    labels = [
        "Family topic pool",
        "Macro-target alignment",
        "Core claim/design alignment",
        "Method/metric alignment",
        "Strict direct effect",
    ]
    counts = [row["claim_pairs"] for row in funnel]
    shares = [100 * row["share_of_universe"] for row in funnel]
    colors = ["#0072B2", "#56B4E9", "#009E73", "#E69F00", "#D55E00"]
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8})
    fig, ax = plt.subplots(figsize=(6.15, 2.55), layout="constrained")
    y = np.arange(len(labels))
    for i, (share, color) in enumerate(zip(shares, colors, strict=True)):
        ax.barh(y[i], share, height=0.52, color=color, edgecolor="none", zorder=3)
        formatted = f"{counts[i]:,} pairs ({share:.1f}%)" if share >= 1 else (
            f"{counts[i]:,} pairs ({share:.3g}%)" if share else "0 pairs (0%)"
        )
        ax.text(min(share + 1.2, 68), y[i], formatted, va="center", ha="left", fontsize=7.2)
    ax.set_yticks(y, labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xticks([0, 25, 50, 75, 100], ["0", "25", "50", "75", "100"])
    ax.set_xlabel("Share of the 13,873 cross-paper claim-pair universe (%)")
    ax.grid(axis="x", color="#D9DDE2", linewidth=0.6, zorder=0)
    ax.set_axisbelow(True)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0, pad=5)
    fig.savefig(figure_dir / "Figure_1_alignment_funnel.png", dpi=600)
    plt.close(fig)

    fields = results["table_6_blockers"]
    y = np.arange(len(fields))
    applicable = np.array([row["applicable_pairs"] for row in fields], dtype=float)
    missing = np.array([row["missing_pairs"] for row in fields], dtype=float) / applicable * 100
    different = np.array([row["different_present_value_pairs"] for row in fields], dtype=float) / applicable * 100
    unblocked = np.array([row["unblocked_applicable_pairs"] for row in fields], dtype=float) / applicable * 100
    fig, ax = plt.subplots(figsize=(6.15, 3.35), layout="constrained")
    ax.barh(y, missing, color="#0072B2", edgecolor="white", linewidth=0.25, label="Missing")
    ax.barh(y, different, left=missing, color="#E69F00", edgecolor="white", linewidth=0.25,
            label="Different present values")
    ax.barh(y, unblocked, left=missing + different, color="#009E73", edgecolor="white", linewidth=0.25,
            label="Unblocked")
    ax.set_yticks(y, [row["label"] for row in fields])
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xticks([0, 25, 50, 75, 100], ["0%", "25%", "50%", "75%", "100%"])
    ax.set_xlabel("Share of applicable claim pairs")
    ax.grid(axis="x", color="#D9DDE2", linewidth=0.55, zorder=0)
    ax.set_axisbelow(True)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0, pad=5)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.005), ncol=3, frameon=False, fontsize=7.2)
    for i, count in enumerate(applicable.astype(int)):
        ax.text(102, i, f"n={count:,}", va="center", ha="left", fontsize=7.0, clip_on=False)
    fig.savefig(figure_dir / "Figure_2_blocker_composition.png", dpi=600)
    plt.close(fig)

    transitions = results["contract_verdicts_and_transitions"]["transition_matrices"]
    fig, axes = plt.subplots(1, 3, figsize=(8.2, 2.8), layout="constrained")
    for ax, (label, matrix) in zip(axes, transitions.items(), strict=True):
        order = ["incomparable", "insufficient_information"]
        values = np.array([[matrix.get(a, {}).get(b, 0) for b in order] for a in order])
        ax.imshow(values, cmap="Blues", vmin=0, vmax=max(1, int(values.max())))
        ax.set_title(label.replace("_to_", " → "))
        ax.set_xticks(range(2), ["Incomparable", "Insufficient"], rotation=25, ha="right")
        ax.set_yticks(range(2), ["Incomparable", "Insufficient"])
        ax.set_xlabel("Destination verdict")
        ax.set_ylabel("Source verdict")
        for i in range(2):
            for j in range(2):
                ax.text(j, i, f"{values[i, j]:,}", ha="center", va="center", fontsize=7)
    fig.savefig(figure_dir / "Figure_S1_contract_transitions.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.15, 3.35), layout="constrained")
    for family, color in (("F1", "#111111"), ("F2", "#777777")):
        for field, style, label in (
            ("applicable_benchmark_assessability_score", "-", "weighted"),
            ("equal_weight_applicable_score", "--", "equal-weight"),
        ):
            values = np.sort(
                np.array(
                    [
                        float(row[field])
                        for row in ba_rows
                        if row["family"] == family
                    ],
                    dtype=float,
                )
            )
            y_ecdf = np.arange(1, len(values) + 1) / len(values)
            ax.step(
                values,
                y_ecdf,
                where="post",
                label=f"{family} {label}",
                color=color,
                linestyle=style,
                linewidth=1.8,
            )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Benchmark-assessability score")
    ax.set_ylabel("Empirical cumulative proportion")
    ax.grid(color="#D9DDE2", linewidth=0.55)
    ax.legend(frameon=False)
    fig.savefig(figure_dir / "Figure_S2_BA_distribution.png", dpi=300)
    plt.close(fig)


def write_outputs(results: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "results.json").write_text(
        json.dumps(results, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    table3_rows = [
        {"dimension": dimension, "category": value, "claims": count}
        for dimension, values in results["table_3_claim_dimensions"].items()
        for value, count in values.items()
    ]
    write_tsv(out_dir / "table_3_claim_dimensions.tsv", table3_rows)
    write_tsv(
        out_dir / "table_4_missing_required_values.tsv",
        [
            {"missing_field": path, "claims": count}
            for path, count in results["table_4_missing_claim_values"].items()
        ],
    )
    write_tsv(out_dir / "table_5_evidence_alignment_funnel.tsv",
              results["table_5_evidence_alignment_funnel"])
    write_tsv(out_dir / "table_6_blockers.tsv", results["table_6_blockers"])
    write_tsv(
        out_dir / "contract_verdicts.tsv",
        [
            {"contract": contract, "verdict": verdict, "pairs": count}
            for contract, verdicts in results["contract_verdicts_and_transitions"]["verdict_counts"].items()
            for verdict, count in verdicts.items()
        ],
    )
    write_tsv(
        out_dir / "contract_transitions.tsv",
        [
            {"transition": transition, "changed_pairs": count}
            for transition, count in results["contract_verdicts_and_transitions"]["changed_pair_counts"].items()
        ],
    )
    write_tsv(
        out_dir / "benchmark_assessability.tsv",
        [
            {"group": group, "mean_score": score}
            for group, score in results["benchmark_assessability"]["weighted_mean"].items()
        ]
        + [{"group": "all_equal_weight", "mean_score": results["benchmark_assessability"]["equal_weight_mean"]}],
    )
    write_tsv(out_dir / "field_ablation_by_path.tsv", results["field_ablation_by_path"])
    write_tsv(
        out_dir / "identifier_ablation.tsv",
        [
            {
                "policy": policy_name,
                "population": population,
                "n_pairs": population_result["n_pairs"],
                **population_result["outcomes"],
            }
            for policy_name, policy_result in results["identifier_ablation"]["policies"].items()
            for population, population_result in policy_result["population_results"].items()
        ],
    )
    generate_figures(results, out_dir)
    output_files = [
        path
        for path in sorted(out_dir.rglob("*"))
        if path.is_file()
        and path.name != "output_manifest.json"
        and ".matplotlib" not in path.relative_to(out_dir).parts
    ]
    manifest = {
        "schema_version": "financialqml-reproduction-output-manifest-v1",
        "frozen_analysis_inputs_sha256": FROZEN_INPUTS_SHA256,
        "input_manifest_sha256": INPUT_MANIFEST_SHA256,
        "article_source_sha256": sha256(DATA / "FinancialQML_EPJQT.md"),
        "code_sha256": sha256(Path(__file__)),
        "runtime": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "numpy": importlib.metadata.version("numpy"),
            "matplotlib": importlib.metadata.version("matplotlib"),
        },
        "outputs": [
            {"path": path.relative_to(out_dir).as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)}
            for path in output_files
        ],
    }
    (out_dir / "output_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return None


def reproduce(out_dir: Path = DEFAULT_OUT) -> dict[str, Any]:
    results = compute_results()
    write_outputs(results, out_dir)
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="verify checksums and archive integrity without recomputing results",
    )
    args = parser.parse_args()
    if args.verify_only:
        verify_archive()
        print("All frozen input checksums and archive members verified.")
        return
    print(json.dumps(reproduce(args.out), indent=2, sort_keys=True, ensure_ascii=False))


if __name__ == "__main__":
    main()
