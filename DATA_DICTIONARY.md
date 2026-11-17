# Data files

| File | Contents |
|---|---|
| `data/FinancialQML_EPJQT.md` | Packaged manuscript source, including its research declarations. |
| `data/article-manifest.json` | Manuscript checksum, corpus counts, contracts, data-archive DOI, and code-release citation for this snapshot. |
| `data/input_manifest.json` | SHA-256 and byte size for each packaged data input. |
| `data/frozen_analysis_inputs.zip` | Frozen paper registry, contract-pair records, field-ablation results, and an internal hash manifest. |
| `data/article-profiles.json` | Accepted structured claim profiles used in the current manuscript analysis. |
| `data/article-pair-diagnostics.json` | Pair-level diagnostic records used to recompute the alignment funnel and field partitions. |
| `data/claim-paper-map.json` | Mapping from each claim identifier to its paper identity and study family. |
| `data/finance-v9-applicability-summary.json` | Frozen expected field-applicability counts used to check blocker calculations. |
| `data/ba-scores.tsv` and `data/ba-summary.json` | Per-claim and aggregate benchmark-assessability scores. |
| `data/identifier-ablation-results.json` | Frozen identifier-omission sensitivity results. |

The 240 claim profiles generate 14,280 within-family claim combinations before excluding within-paper combinations; the cross-paper analysis universe contains 13,873 pairs. Records are structured and source-linked in the study materials, but this release does not include source PDFs, full-text passages, or verbatim quotations.
