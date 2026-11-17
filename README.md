# FinancialQML reproducibility package

This repository contains the frozen inputs, deterministic analysis code, and manuscript source for *From Demonstrations to Comparable Evidence in Financial Quantum Machine Learning and Computing*.

It reproduces the manuscript's tabulations, comparison-contract results, sensitivity summaries, and figures from the included structured records. It does not retrieve or redistribute source papers. The manuscript describes the study methods and reports the applicable research disclosures.

In the research workflow, large language models assisted with structured claim extraction and candidate generation. This release provides the resulting frozen records and deterministic downstream analysis; it does not rerun those language-model-assisted steps.

## Reproduce the analysis

Requirements: Python 3.13.11. Install the pinned runtime and test packages from `requirements-dev.txt` to run the complete verification below.

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
make verify
make test
make reproduce
```

On Windows, create the environment with `py -3.13 -m venv .venv` and activate it with `.venv\Scripts\activate`. Docker is also supported:

```bash
docker build -t financialqml-reproducibility .
docker run --rm -v "$PWD/outputs:/release/outputs" financialqml-reproducibility
```

The main output is written to `outputs/reproduced/`. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for the exact reproduction scope, expected counts, and output inventory.

## Frozen study snapshot

The packaged manuscript and inputs correspond to the 56-paper, 240-claim study snapshot. The cross-paper universe contains 13,873 claim pairs. The alignment funnel contains 13,873, 3,451, 510, 5, and 0 pairs across its successive tiers. The three comparison contracts produce no comparable pairs under their defined rules. Every input is checked against SHA-256 checksums before analysis.

The structured dataset is archived at [Zenodo, DOI 10.5281/zenodo.23811821](https://doi.org/10.5281/zenodo.23811821). Code is licensed under Apache-2.0. The structured research data are licensed under CC BY 4.0; see [DATA_LICENSE.md](DATA_LICENSE.md). Manuscript rights are separate from these licenses.

The public release repository is [github.com/rtales/FinancialQML-reproducibility](https://github.com/rtales/FinancialQML-reproducibility). The manuscript cites release `v1.0.1` as its code and frozen-input version.

## Repository contents

- `src/` — deterministic analysis and artifact generation.
- `tests/` — checks for input integrity and manuscript-reported results.
- `data/` — frozen analysis inputs, checksums, and manuscript source.
- `outputs/` — generated results (created when reproduction runs).
- `REPOSITORY_MAINTENANCE.md` — maintenance rule for the separate private development and public release repositories.

The continuous-integration workflow verifies frozen inputs, runs the test suite, recomputes the outputs, and exercises the Docker image.
