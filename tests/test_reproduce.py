from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.reproduce import compute_results, verify_archive, write_outputs


@pytest.fixture(scope="session")
def results():
    return compute_results()


def test_frozen_data_archive_and_manifest():
    verify_archive()


def test_public_package_contains_clean_analysis_records_without_run_traces():
    data = Path(__file__).resolve().parents[1] / "data"
    excluded = {
        "source_run",
        "claim_path",
        "left_run",
        "right_run",
        "left_paper_id",
        "right_paper_id",
        "created_utc",
    }
    for filename in (
        "article-profiles.json",
        "article-pair-diagnostics.json",
        "claim-paper-map.json",
    ):
        rows = json.loads((data / filename).read_text(encoding="utf-8"))
        assert all(not (excluded & row.keys()) for row in rows)
    sensitivity = json.loads((data / "identifier-ablation-results.json").read_text(encoding="utf-8"))
    assert sensitivity["analysis_type"] == "post-hoc descriptive sensitivity analysis"
    assert not ({"created_utc", "input_sha256", "protocol_sha256", "script_sha256"} & sensitivity.keys())
    with zipfile.ZipFile(data / "frozen_analysis_inputs.zip") as archive:
        assert set(archive.namelist()) == {
            "contract_pairs.json",
            "field_ablation_results.json",
            "FROZEN_INPUTS_MANIFEST.json",
        }


def test_corpus_and_funnel_match_the_manuscript(results):
    assert results["corpus"] == {
        "papers": 56,
        "claims": 240,
        "quote_verified_claims": 240,
        "papers_by_family": {"F1": 28, "F2": 28},
        "claims_by_family": {"F1": 120, "F2": 120},
        "cross_paper_claim_pairs": 13873,
    }
    assert [row["claim_pairs"] for row in results["table_5_evidence_alignment_funnel"]] == [
        13873,
        3451,
        510,
        5,
        0,
    ]
    assert [row["paper_pairs"] for row in results["table_5_evidence_alignment_funnel"]] == [
        756,
        756,
        302,
        4,
        0,
    ]


def test_table_three_claim_dimensions(results):
    assert results["table_3_claim_dimensions"]["claim_target"] == {
        "feasibility": 56,
        "computational_cost": 54,
        "pricing_accuracy": 38,
        "solution_quality": 33,
        "economic_performance": 30,
        "resource_requirement": 29,
    }
    assert results["table_3_claim_dimensions"]["result_basis"] == {
        "observed_hardware": 86,
        "observed_simulation": 75,
        "simulation_based_projection": 42,
        "theoretical_projection": 24,
        "mixed": 13,
    }


def test_table_four_missing_required_values(results):
    assert results["table_4_missing_claim_values"] == {
        "subject_method.algorithm_id": 234,
        "metric.metric_id": 230,
        "metric.definition_ref": 214,
        "subject_method.implementation_protocol_id": 172,
        "metric.unit": 127,
        "comparator.protocol_id": 97,
        "comparator.method_id": 92,
        "scale.n_assets": 72,
        "finance_context.objective_id": 62,
        "finance_context.constraints_id": 59,
    }


def test_table_six_pair_field_partitions(results):
    by_field = {row["field"]: row for row in results["table_6_blockers"]}
    assert (
        by_field["scale.n_assets"]["applicable_pairs"],
        by_field["scale.n_assets"]["missing_pairs"],
        by_field["scale.n_assets"]["different_present_value_pairs"],
        by_field["scale.n_assets"]["unblocked_applicable_pairs"],
    ) == (12750, 7270, 5049, 431)
    assert (
        by_field["claim_target"]["applicable_pairs"],
        by_field["claim_target"]["missing_pairs"],
        by_field["claim_target"]["different_present_value_pairs"],
        by_field["claim_target"]["unblocked_applicable_pairs"],
    ) == (13873, 0, 10422, 3451)


def test_contract_outcomes_transitions_and_secondary_metrics(results):
    contract = results["contract_verdicts_and_transitions"]
    assert contract["verdict_counts"] == {
        "L0": {"comparable": 0, "insufficient_information": 81, "incomparable": 13792},
        "T1": {"comparable": 0, "insufficient_information": 60, "incomparable": 13813},
        "I1": {"comparable": 0, "insufficient_information": 44, "incomparable": 13829},
    }
    assert contract["changed_pair_counts"] == {
        "L0_to_T1": 71,
        "L0_to_I1": 59,
        "T1_to_I1": 16,
    }
    assert results["benchmark_assessability"] == {
        "weighted_mean": {"all": 0.8418, "F1": 0.8345, "F2": 0.8491},
        "equal_weight_mean": 0.8274,
    }
    assert results["field_ablation_verdicts"] == {
        "comparable": 0,
        "incomparable": 13792,
        "insufficient_information": 81,
    }
    assert len(results["field_ablation_by_path"]) == 36
    assert all(row["counterfactual_comparable"] == 0 for row in results["field_ablation_by_path"])
    identifier = results["identifier_ablation"]["policies"]
    assert len(identifier) == 2
    assert all(
        result["outcomes"]["counterfactual_blocker_free"] == 0
        for policy in identifier.values()
        for result in policy["population_results"].values()
    )


def test_all_tables_figures_and_output_manifest_are_written(results, tmp_path: Path):
    write_outputs(results, tmp_path)
    expected = {
        "Figure_1_alignment_funnel.png",
        "Figure_2_blocker_composition.png",
        "Figure_S1_contract_transitions.png",
        "Figure_S2_BA_distribution.png",
    }
    files = {path.name for path in (tmp_path / "figures").glob("*.png")}
    assert files == expected
    assert all((tmp_path / "figures" / name).stat().st_size > 10_000 for name in expected)
    for name in (
        "results.json",
        "table_3_claim_dimensions.tsv",
        "table_4_missing_required_values.tsv",
        "table_5_evidence_alignment_funnel.tsv",
        "table_6_blockers.tsv",
        "contract_verdicts.tsv",
        "contract_transitions.tsv",
        "benchmark_assessability.tsv",
        "field_ablation_by_path.tsv",
        "identifier_ablation.tsv",
        "output_manifest.json",
    ):
        assert (tmp_path / name).is_file()
