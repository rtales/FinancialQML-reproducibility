# Reproduction protocol

## Scope

This package independently reproduces the deterministic analysis reported in the packaged manuscript from versioned structured records. In the research workflow, large language models assisted with structured claim extraction and candidate generation; this package does not rerun those steps and instead uses the frozen structured records they produced. It checks the input archive, individual input files, manuscript checksum, and frozen reference summaries before computing results.

The release does not rerun document retrieval, full-text screening, or claim extraction from source publications. It includes the accepted structured claim profiles and comparison diagnostics required for the computations. Source PDFs, full-text passages, and verbatim claim quotations are not redistributed. Reproduction of the deterministic analysis therefore does not require model calls or access to external APIs.

## Environment

- Python 3.13.11
- Runtime packages pinned in `requirements.txt`; test dependencies are pinned in `requirements-dev.txt`
- Container recipe in `Dockerfile`

The analysis script makes no network requests. Install the pinned development dependencies first:

```bash
python -m pip install -r requirements-dev.txt
```

Then the following commands run offline:

```bash
make verify
make test
make reproduce
```

`make reproduce` writes results under `outputs/reproduced/`. To choose another destination:

```bash
python src/reproduce.py --out /path/to/output
```

To verify inputs without running the analysis:

```bash
python src/reproduce.py --verify-only
```

## Expected results

The run should report:

- 56 papers, evenly divided between F1 and F2;
- 240 claims, evenly divided between F1 and F2;
- 13,873 cross-paper claim pairs;
- funnel counts of 13,873 → 3,451 → 510 → 5 → 0;
- zero `comparable` verdicts under each of L0, T1, and I1.

The tests also check claim-dimension counts, missing-value counts, pair-level blocker partitions, verdict transitions, benchmark-assessability summaries, and sensitivity results. A failing assertion indicates that the computation no longer agrees with this frozen manuscript snapshot.

## Generated artifacts

The output directory contains `results.json`, tabular files for manuscript results, four publication-resolution PNG figures, and `output_manifest.json`. The manifest records SHA-256 hashes and byte sizes for the generated artifacts and records the runtime versions. Numeric and tabular outputs are the primary comparison targets. Image bytes can vary across operating systems or graphics-library builds even when the underlying plotted data are identical.

The bundled tests verify that all expected tables and figures are created. The CI workflow also builds and executes the Docker image so the containerized path is checked on the hosted Linux runner.

## Data provenance

`data/input_manifest.json` pins every packaged input. `data/frozen_analysis_inputs.zip` contains the exact reference records needed for the contract and field-ablation computations, plus its own member manifest. `data/article-manifest.json` records the manuscript checksum and snapshot counts. The structured data archive is cited in the article and available from [Zenodo](https://doi.org/10.5281/zenodo.23811821).
