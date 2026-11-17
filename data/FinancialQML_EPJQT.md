# From Demonstrations to Comparable Evidence in Financial Quantum Machine Learning and Computing

## A Quote-Verified Claim-Level Audit of Portfolio Optimization and Derivative Pricing Studies

Tales Matos (1); Victor Oliveira Santos (1); Jesse Van Griensven Thé (3); Jose Antonio Macedo (2); Bahram Gharabaghi (1, corresponding author)

Tales Matos: tbenigno@uoguelph.ca
Victor Oliveira Santos: volive04@uoguelph.ca
Bahram Gharabaghi: bgharaba@uoguelph.ca
Jesse Van Griensven Thé: Jesse.the@weblakes.com
Jose Antonio Macedo: jose.macedo@insightlab.ufc.br

1. Department of Civil, Environmental and Water Resources Engineering, College of Engineering, University of Guelph, 50 Stone Rd E, Guelph, ON N1G 2W1, Canada
2. Federal University of Ceará, Department of Computing, Campus do Pici, Fortaleza-CE 60440-900, Brazil
3. Lakes Environmental, 170 Columbia St. W, Waterloo, ON N2L 3L3, Canada

Correspondence: Bahram Gharabaghi, bgharaba@uoguelph.ca

## Abstract

Financial quantum computing studies span financial tasks, methods and evaluation designs whose results cannot be compared from application labels alone. We introduce an auditable claim-level framework for determining when reported effects support a stated cross-study comparison, and apply it to a purposive, balanced corpus of 56 portfolio-optimization and derivative-pricing papers. Source-verified extraction and adjudication produced 240 claims and 13,873 within-family cross-paper claim pairs. The alignment funnel identified 3,451 macro-target pairs, 510 core claim/design pairs and 5 method/metric pairs; none met the predefined exact-value L0 contract. A post-hoc stored-blocker sensitivity left no blocker-free pair after omitting either six core identifier paths or all L0 paths ending in `_id` or `_ref`. In a prospectively specified, source-anchored follow-up, 44 scalar assignments were independently reviewed across twelve cases: 20 stored values were updated, and 24 were reassigned unchanged. No pair met any of the three operational contracts in the 30-pair pilot. These findings distinguish topical overlap, recorded heterogeneity and unresolved information. The framework contributes an inspectable schema, comparison-purpose contracts, a field-level blocker taxonomy and reporting guidance for building cumulative evidence while preserving methodological diversity. It assesses cross-study comparability, not quantum-computing performance.

Keywords: financial quantum computing; quantum machine learning; portfolio optimization; derivative pricing; evidence synthesis; benchmarking; reproducibility

## 1. Introduction

Financial quantum machine learning and quantum computing for finance now encompass optimization, simulation, machine learning and resource-estimation studies [1-9]. Portfolio studies use annealing, variational algorithms and gate-model constructions to represent constrained investment problems; derivative studies use amplitude estimation, quantum Monte Carlo, PDE encodings and resource analyses to address valuation and related computations [1-5]. This diversity is scientifically productive, but a common application label does not make reported effects comparable.

Two portfolio papers may respectively report solver quality on synthetic QUBO instances and out-of-sample risk-return performance on historical equities. Two pricing papers may address the same contract family while differing in dynamics, pricing measure, error target, scale, evaluation basis or cost boundary. In each case, thematic proximity coexists with different scientific objects. A cumulative evidence base therefore needs explicit positive, negative and insufficient-information decisions about the relation between situated claims.

We ask: given source-verified Financial QML/QC claims, how often do claims satisfy an explicit instrument for direct effect-level comparison, and which dimensions determine the result? We address this question in two families: portfolio optimization (F1) and derivative pricing (F2). Claims, rather than papers, are the unit of comparison because a single paper may report effects with different targets, metrics and evidentiary bases.

This claim-level view captures both diversity within papers and potential links across them. A hardware observation, a simulated pricing error, an asymptotic resource claim and an economic backtest each require a distinct comparison context; claims in different papers can nevertheless be related when their targets, protocols and measurement semantics align. An explicit relation records both the basis for comparison and the dimensions that prevent it.

The study contributes: (1) a finance-specific claim schema covering task, method, evaluation, metric, baseline, scale, cost and provenance; (2) an evidence-alignment funnel that distinguishes thematic relatedness from progressively stronger operational alignment; (3) a source-verified audit of 56 papers and 240 claims, with field-level blocker accounting and a prospective twelve-case reconstruction; and (4) a reporting instrument that makes comparison decisions inspectable. Together, these contributions show how to identify where published claims align, where recorded results differ and where additional information is needed before synthesis.

## 2. Related Work

### 2.1 Financial tasks and quantum methods

The financial object must be specified before computational performance can be interpreted. Mean-variance portfolio selection jointly treats expected return and risk [10], while option valuation depends on the contract and assumptions that define its price [11]. Monte Carlo implementations introduce choices about path generation, discretization and variance reduction [12]. These foundations motivate recording financial context and baseline assumptions alongside an algorithm label.

Portfolio formulations illustrate several comparison dimensions. Multi-period allocation and rebalancing can include transaction costs and market impact [13-14], while backtesting adds a temporal evaluation protocol [15]. The inclusion boundary is the decision object: F1 includes choices over portfolio holdings or weights, including multi-period rebalancing, and excludes execution-only trajectories, market-microstructure strategies and trading-signal studies without a portfolio-allocation decision. Annealing controls affect success and chain-break behaviour [16]; QAOA and VQE studies expose choices in ansatz, classical optimization, sampling, noise and hyperparameters [17-18]. A solver objective, an execution-quality metric and an investment-performance metric are therefore not interchangeable simply because each concerns portfolios.

Derivative-pricing studies are similarly heterogeneous. Least-squares Monte Carlo estimates continuation values for early exercise [19], whereas Bermudan pricing with quantum amplitude estimation uses Chebyshev interpolation [20]. Local-volatility work compares state-preparation strategies and fault-tolerant resources [21]. Unary asset representations and signed-payoff encodings create further distinctions [22-23]. Contract semantics, dynamics, encoding and resource assumptions determine what a reported pricing effect means.

Quantum Monte Carlo speedups depend on the estimation and access model [24]. Amplitude-estimation variants use different classical processing, error control and sign handling [25-27]. Resource studies expose costs beyond asymptotic query scaling [28], and iterative amplitude estimation may exhibit stopping-rule bias [29]. These results make error target, confidence, variance, and cost scope necessary context for comparing sampling-efficiency claims. They also show why a comparison purpose that treats algorithm identity as a treatment differs from one that requires the same implementation.

### 2.2 Structured reporting and reusable evidence

Model cards and datasheets make evaluation conditions, intended uses and data properties explicit [30-31]. Systematic-review and mapping guidance similarly emphasizes transparent search, inclusion, extraction and synthesis decisions [32-34]. FAIR principles connect reuse to identifiers, metadata and provenance [35]. The Machine Learning Reproducibility Checklist addresses computational experiments within papers [36], while the Open Research Knowledge Graph represents scholarly contributions in machine-actionable form [37]. We adapt this logic to a narrower object: the fields needed to decide whether two finance-related quantum claims support a stated comparison.

Scientific-claim verification links assertions to evidence and rationales [38]. ERASER distinguishes evidence agreement from rationale faithfulness [39]. These precedents motivate evidence spans and isolated review. PRISMA-S specifies reproducible search reporting [40], and SWiM addresses transparent synthesis without meta-analysis [41]. We adapt these complementary principles to a claim-comparability audit through explicit decisions and traceable records.

Standardization in quantum technologies emphasizes harmonized terminology, methods, and interfaces [42]. Such work provides interoperability context rather than validation of the particular comparison rules used here. Our instrument retains unresolved mappings rather than forcing a shared identifier when source-local terminology cannot be uniquely resolved.

Engineering treatments of quantum circuits, data encoding, optimization and quantum neural networks provide useful technical vocabulary [43]. Still, a common vocabulary alone does not resolve whether two financial results estimate the same effect. Stable identifiers must preserve version and meaning, and a local definition must remain local unless an evidence-backed mapping establishes equivalence. This is particularly important for metric labels that can denote different numerators, denominators, aggregation rules or cost boundaries across studies.

### 2.3 Quantum benchmarking and the unresolved gap

Quantum benchmarking requires specified tasks, baselines, metrics and resource assumptions. QOBLIB provides a broad optimization-benchmarking framework [44], while systematic recommendations, scalable benchmark suites and QML-specific analyses emphasize workload construction and classical baselines [45-47]. Application-oriented benchmarks measure execution quality and time to solution across workloads [48]. Financial applications add domain requirements such as asset universes, temporal protocols, contract families, payoff definitions, calibration, market data and economic cost boundaries.

Definitions of quantum speedup depend on the comparator and benchmark construction [49]. Certification protocols vary in information and resource requirements [50]; processor-capability measures depend on program structure [51]; and emulator-to-hardware comparisons depend on noise-model selection [52]. Critiques of advantage-focused QML evaluation caution against extrapolating from restricted settings to practical usefulness [53]. A recent portfolio benchmark likewise shows that conclusions depend on formulation, baselines, instances and tested scale [54]. CLAIMSTAB-QC audits source-bounded comparative claims in quantum-software papers, distinguishing claims that can be planned for audit from those with enough matched evidence to assess the reported relation [55]. Its unit is a comparison reported in a source paper; the present study instead asks whether claims from different financial-QML and quantum-finance papers share the fields required for a stated cross-study comparison. Of 455 claims examined by CLAIMSTAB-QC, eight exposed enough matched evidence to audit the original comparison; those yielded two Sustained, four Unresolved and two Reversed outcomes [55]. The differing outcome distributions reflect distinct questions and audit units, not a direct comparison of framework performance.

Together, this literature motivates an intermediate layer between reporting guidance and common-workload benchmarks: a method for testing whether published claim records share the conditions needed for a stated comparison. We operationalize this layer for portfolio optimization and derivative pricing, diagnosing compatibility across existing reports and translating the results into field-level reporting requirements.

The gap is therefore between reporting guidance and comparison execution. Existing standards can recommend that authors disclose context, and benchmark libraries can define new common tasks retrospectively. However, retrospective evidence synthesis still requires a rule that turns reported fields into a contestable relation. Our funnel provides that rule at progressively stronger levels. Its blocker profiles map the conditions for stronger alignment to specific fields and source evidence, guiding both reusable mappings and more informative reporting.

## 3. Scope and Definitions

Financial QML/QC denotes quantum-machine-learning and quantum-computing methods applied to financial tasks, including gate-model algorithms, annealing, simulation, amplitude estimation, variational methods and resource-estimation claims. Here, “QML” means quantum machine learning; quantile machine learning is outside this review’s scope. We also exclude quantum-inspired methods when they are the evaluated arm. Classical baselines may include quantum- or annealing-inspired heuristics when used as comparators by a source paper.

F1 covers portfolio selection, index tracking, asset allocation, QUBO portfolio formulations and related investment optimization. F2 covers option pricing, derivative valuation, pricing accuracy, pricing resource estimates and related simulation or PDE claims. Execution-only trading trajectories, market-microstructure strategies and trading-signal studies without a portfolio-allocation decision, as well as fraud, credit, insurance, macro-finance and broader risk applications, lie outside this two-family audit. Portfolio allocation or rebalancing remains within F1 when it is the evaluated financial decision, even when transaction costs or multiple periods are modelled.

Direct effect-level comparability is a typed relation, not a property of a paper. Under the predefined exact-match contract (L0), two claims are comparable only when their stored information supports the same kind of effect under compatible task, metric, result basis, evaluation design, cost scope, computational model, baseline, scale and finance context. This conservative definition is stricter than thematic or narrative similarity.

## 4. Methods

### 4.1 Corpus construction

The frozen corpus contains 56 unique papers, 28 in each family. DOI, arXiv identifier and normalized title provide deduplication fallbacks. Inclusion required an applied F1 or F2 task, an evaluated quantum computing, QML, annealing, simulation or resource-estimation component, and obtainable source text. Preprints and journal articles were eligible. We excluded generic algorithms without a financial task, quantum-inspired evaluated arms, and applications outside F1/F2.

Paper-level corpus assembly and claim-level extraction followed distinct, predefined stages. Prespecified claim-slot passes expanded the accepted evidence across scientific objects within the 56 selected papers, with bounded recovery of technical failures. This process yielded 240 accepted claims, 120 per family. The resulting balanced corpus enables claim-level analysis across portfolio optimization and derivative pricing. Supplement S1 documents the corpus design and full profile distributions. Supplementary methods and evidence are provided in Additional file 1, and the itemized 56-paper corpus register is provided in Additional file 2.

### 4.2 Claim representation and source verification

Each record represents one assertion and stores its claim target and detail; method, algorithm surface, paradigm and computational model; task, backend, evaluation design and problem family; finance and market context; metric name, unit, definition and direction; comparator; scale; result basis; cost scope; and evidence spans. Claim-level representation is necessary because a paper may contain effects with different targets, metrics and evidentiary bases.

The schema separates a human-readable surface from a canonical field wherever a stable mapping may exist. For example, an algorithm name can be retained even when no unique registry identifier is available, and a metric can retain its reported label, unit and source-local definition without being promoted to a shared semantic identifier. This prevents a resolver failure from erasing source content while also preventing textual resemblance from being mistaken for equivalence. Finance-specific fields preserve portfolio objectives, constraints, universes and temporal designs or, for derivatives, contract, payoff, underlying, dynamics, calibration, maturity, moneyness and discretization.

A source-verified record links each claim and populated field to spans in the frozen source text and validates against the typed schema. These links make the evidence basis inspectable while retaining source-local terminology and context.

Extraction used three isolated annotation passes followed by adjudication of anonymized candidates. A deterministic resolver populated identifiers only after a unique normalized label or alias match in the F1/F2 pilot registry; ambiguous and unmatched surfaces retained their source labels without a canonical identifier. The pilot vocabulary contains 10 algorithm, 10 metric, 7 comparator, 3 objective, 6 derivative-contract and 3 dynamics-model entries (Supplement S2).

In the resolved profile, algorithm surfaces were populated in 240 of 240 claims and algorithm IDs in 6; metric surfaces were populated in 240 and metric IDs in 10; comparator-method surfaces were populated in 204 and method IDs in 8. Among 95 comparative claims with a nonblank comparator-method surface, no comparator-protocol ID was populated. No pre-resolution algorithm, metric or comparator-method IDs were supplied, so populated IDs reflect unique registry matches. These record-level surface and resolution counts are reported by family in Supplement S11; an empty canonical-ID field is distinct from an empty surface field. Pairwise comparison and aggregation were deterministic after extraction and resolution. Supplement S5 documents the historical cross-model consistency review.

### 4.3 Comparison contracts

For every within-family pair, L0 selects target-specific required paths and evaluates their union. A path is missing if either stored value is null and different if both values are present but unequal. A known difference produces `incomparable`; with no known difference, missing required information produces `insufficient information`; complete alignment produces `comparable`. Diagnostics retain both missing and differing paths even when a difference already determines the verdict.

Comparison uses exact resolved values. L0 does not apply numerical tolerances, unit conversion, interpolation, overlap analysis or curve comparison. Common requirements include algorithm identity and metric identifiers; finance and scale requirements depend on the target. Under L0, only a null value is missing; every non-null value is compared literally, including blank strings and sentinel strings such as `unstated`. The funnel tiers reuse the L0 blocker vector, so a shared sentinel can pass an intermediate tier without establishing substantive alignment. T1 and I1 instead treat nulls, blank strings and configured unknown tokens, including `unstated`, as missing. Backend modality and metric direction are recorded but are not independent L0 equality checks. The exact target-specific L0 paths are listed in Supplement S2.2; the separately sealed T1/I1 follow-up rules are summarized in S2.3.

The decision precedence is deliberately asymmetric. A known disqualifying difference is sufficient for an incomparable verdict even if other required paths are missing, but the missing paths remain visible in the blocker vector. When no known difference exists, a required unknown prevents a positive verdict. Only complete applicable alignment yields comparable. Null required values prevent a positive verdict, while non-null sentinel strings are compared literally under L0 and may pass an intermediate funnel tier. The diagnostic record therefore distinguishes missing values from recorded differences and retains both in its blocker vector.

The prospective follow-up also tested two sealed operational contracts. T1 compares task and outcome fields while treating algorithm and implementation as treatments; I1 adds explicit implementation alignment. Both use exact stored-value equality, retain missing and differing blockers, and apply known-difference-before-missing precedence. Neither converts units or applies numerical tolerances. For specified pricing-accuracy, resource, cost and feasibility cases, T1 and I1 require a confidence field. Its observed missingness and co-occurring blockers are quantified in Supplement S11.2. Table 1 summarizes their purpose; Supplement S2.3 gives the frozen fields and conditions. These are operational diagnostics, not validated universal standards.

**Table 1. Operational comparison purposes and requirements.**

| Contract | Comparison purpose | Required information | Decision rule and boundary |
| --- | --- | --- | --- |
| L0 | Strict record-level alignment | Common finance application, claim target, algorithm ID, computational model, evaluation design, metric ID, definition reference, unit and result basis; target-specific fields and applicable comparator fields | Exact equality on the union of applicable paths; no tolerances, unit conversion, interpolation or curve comparison. |
| T1 | Same task and outcome across potentially different methods | Common application, target and detail, result basis, evaluation design, metric ID, definition reference, unit and direction; target-specific task/finance paths, with conditional scale and confidence fields | Algorithms and implementation are not equality requirements. Exact equality; known mismatch precedes missing information. |
| I1 | Implementation-aligned task and outcome comparison | T1 fields plus algorithm ID, computational model, implementation-protocol ID and backend modality | Exact equality; known mismatch precedes missing information. |

### 4.4 Evidence-alignment funnel and blocker taxonomy

The denominator comprises all within-family, cross-paper claim pairs. Two 28-paper families yield 378 paper pairs each and 756 total. A claim pair survives a tier when no blocker occurs among that tier's applicable paths.

**Table 2. Operational requirements for the evidence-alignment tiers.**

| Tier | Cumulative operational requirement |
| --- | --- |
| Family topic pool | Same family and different canonical papers |
| Macro-target alignment | Equal claim target |
| Core claim/design alignment | Add target detail, result basis and evaluation design |
| Method/metric alignment | Add applicable cost scope, computational model and metric unit |
| Strict direct effect | Complete target-specific contract with neither missing nor different required values |

Paper-pair survival is existential: at least one claim pair between two papers survives. Paper-pair blocker incidence is also existential and may concern another claim pair. All blocker counts are multi-label. The conceptual taxonomy separates scientific heterogeneity, reporting insufficiency and representation or canonicalization gaps, with mixed cases. Because an empty extracted value cannot distinguish absence in the source from extraction or representation loss, the empirical analysis reports missing stored values separately from differences between present values. Source-level attribution requires separate review.

### 4.5 Reproducibility safeguards

Claim membership, source records, the resolver registry and the strict verdict policy are frozen. Content-addressed manifests bind inputs, code, environment and outputs. Deterministic recomputation reconstructs claim profiles, pair membership, complete pair diagnostics and aggregate tables, and rejects drift in bound inputs or comparison policy. Regression tests and independent source-only review check the deterministic analysis against the frozen artifacts.

Each execution records the source versions, accepted-record hashes, registry and policy hashes, software environment and output hashes required to identify the calculation. Completed execution records are immutable, and any rerun uses a new record so that failed attempts and later checks remain distinguishable.

For every pair, the diagnostic blocker vector is the union of all applicable missing paths and all applicable unequal present-value paths. Verdict precedence is evaluated separately as specified in Section 4.3. Retaining both blocker categories supports complete intermediate-tier and frequency summaries without changing the strict verdict calculation. This final representation is applied consistently to funnel survival, blocker counts, applicability denominators and density subsets.

The reproducibility guarantee covers frozen records from structured claim extraction and candidate generation and deterministic downstream recomputation; it does not depend on regenerating identical AI-assisted outputs. Manifests and hashes bind inputs, code, environment and results, while semantic validation is treated separately in Section 8.1.

### 4.6 Prospective anchored source reconstruction

After the original audit result was known, we sealed a follow-up protocol before collecting new annotations or sensitivity counts. Fixed hash ranking selected two distinct papers in each of six family/target strata, yielding twelve assertions from different papers; failed sources could not be replaced. Each packet supplied a preselected source passage without old field values, targets or pair verdicts, while retaining access to the full source. The follow-up therefore evaluates field reconstruction around source anchors.

Three fresh isolated contexts reconstructed eight fields: algorithm surface, metric name, metric definition, metric unit, computational model, cost scope, result basis and evaluation design. We retained typed statuses, quotations, offsets and inspected extents. Deterministic checks verified schema, source identity and quote location; independent adjudication and source review evaluated anonymized proposals, and four fixed cases received an additional audit. The full protocol and field-level decisions are reported in Supplement S6.

Only independently accepted scalar fields could update prior records; composite, unresolved and excluded values retained their original status. The pilot contained 30 within-family cross-paper pairs, alongside a separate suite of synthetic controls. Supplement S6 reports the full overlay and contract results, and Supplement S8 describes the pair structure and residual blockers in the selected sample.

## 5. Results

### 5.1 Corpus and record profile

The 56 papers yielded 240 source-verified claims, evenly divided between F1 and F2 (Table 3). The claims span feasibility, computational cost, pricing accuracy, solution quality, economic performance and resource requirements, with evidence from hardware observations, simulations, projections, backtests and resource estimates. Supplement S1 reports the full profile.

Market context varies across the corpus: 124 records use synthetic settings, 54 have a missing or blank market-region value, 45 concern North America, 7 Europe, 6 Asia-Pacific and 4 a global setting. These profile counts inform the comparison design by showing why market context must be retained at claim level.

**Table 3. Corpus composition and selected record profile.**

| Dimension | Categories and claim counts |
| --- | --- |
| Family | F1 portfolio optimization: 28 papers, 120 claims; F2 derivative pricing: 28 papers, 120 claims |
| Claim target | Feasibility 56; computational cost 54; pricing accuracy 38; solution quality 33; economic performance 30; resource requirement 29 |
| Result basis | Observed hardware 86; observed simulation 75; simulation-based projection 42; theoretical projection 24; mixed 13 |
| Evaluation design | Synthetic benchmark 110; live or paper execution 47; historical backtest 41; resource estimate 30; empirical snapshot 11; unstated 1 |
| Computational model | Gate model 165; quantum annealing 53; unstated 17; analog 3; hybrid 2 |

Canonical identifiers and metric-definition references were sparsely populated in the resolved records: algorithm identifiers appeared in 6 of 240 claims, metric identifiers in 10, and metric-definition references in 26 (Table 4). Claim-level denominators follow each claim's direct-effect requirements and differ from the pairwise union used in Table 6.

**Table 4. Missing required values in resolved records.**

| Field | Missing | Applicable claims |
| --- | ---: | ---: |
| Algorithm identifier | 234 | 240 |
| Metric identifier | 230 | 240 |
| Metric definition reference | 214 | 240 |
| Implementation protocol identifier | 172 | 172 |
| Metric unit | 127 | 240 |
| Comparator protocol identifier | 97 | 97 |
| Comparator method identifier | 92 | 97 |
| Number of assets | 72 | 172 |
| Objective identifier | 62 | 63 |
| Constraints identifier | 59 | 63 |

### 5.2 Evidence alignment under L0

The 240 claims generated 13,873 within-family cross-paper pairs: 6,939 in F1 and 6,934 in F2. All 756 possible within-family paper pairs were represented. Of these claim pairs, 3,451 (24.9%) shared a macro target, 510 (3.7%) met the core claim/design tier and 5 (<0.1%) met the applicable method/metric tier. No pair met the complete strict contract (Table 5).

**Table 5. Cross-paper evidence-alignment funnel.**

| Tier | Claim pairs | F1 | F2 | Paper pairs | Share |
| --- | ---: | ---: | ---: | ---: | ---: |
| Family topic pool | 13,873 | 6,939 | 6,934 | 756 | 100% |
| Macro-target alignment | 3,451 | 1,707 | 1,744 | 756 | 24.9% |
| Core claim/design alignment | 510 | 254 | 256 | 302 | 3.7% |
| Method/metric alignment | 5 | 0 | 5 | 4 | <0.1% |
| Strict direct effect | 0 | 0 | 0 | 0 | 0% |

![FIGURE:Figure 1](figures/Figure_1_alignment_funnel.png)
**Figure 1. Cross-paper evidence-alignment funnel.** Bars show the proportion of the 13,873 cross-paper claim-pair universe reaching each successive tier; labels report exact pair counts. The strict direct-effect tier contains zero pairs.

Adding 407 within-paper pairs gives 14,280 within-family pairs: 3,472 macro-target, 521 core, 7 method/metric and 0 strict survivors. Within the 3,451 macro-target-aligned pairs, 3,370 were incomparable and 81 had insufficient information; no cross-paper pair met L0. Across the full universe, 13,792 of 13,873 pairs had at least one known unequal required value. A predeclared single-field omission diagnostic on the original stored blockers found that removing any one recorded blocker path, in isolation, left every originally blocked pair with at least one blocker (0 of 13,873 became blocker-free); complete field-wise results are in Supplement S9. A separate post-hoc identifier-path omission diagnostic removed either the six core identifier paths or all 15 L0 blocker paths ending in `_id` or `_ref`, leaving all other stored blockers unchanged. Neither omission produced a counterfactual blocker-free pair: the broad omission left 13,790 incomparable and 83 insufficient-information pairs overall, and 3,368 incomparable and 83 insufficient-information pairs among the 3,451 macro-target-aligned pairs. This tests dependence on specified stored fields; it does not establish semantic equivalence. Full path lists, results and hashes are in Supplement S10.

The paper-pair denominator provides a complementary view. Every one of the 756 possible paper pairs had at least one macro-target-aligned claim pair; 302 had at least one core survivor, 4 had at least one method/metric survivor and none had a strict survivor. This reveals widespread topical connection alongside a steep reduction in claim pairs meeting progressively more specific comparison conditions.

All five method/metric survivors belong to F2 and span four paper pairs. Together they contain 57 residual blocker assignments: 50 missing values and 7 differences between present values. Every survivor lacks an algorithm identifier in at least one record; maturity differs in four pairs and contract family in three. Their residual profiles show that potential direct-effect comparisons depend on linked contract, measurement, algorithm and implementation fields, not scale alone. Supplement S3 provides the pair-by-field accounting.

Reduced-density subsets selected at most one or two claims per paper under deterministic priorities. The one-claim subset contained 756 pairs, with 145 core and 4 method/metric survivors; the two-claim subset contained 3,024 pairs, with 235 core and 4 method/metric survivors. Neither contained a strict survivor. Full subset counts and their relation to the full audit are reported in Supplement S3.

### 5.3 Anatomy of blocked comparisons

Table 6 reports blockers over the pairs for which each field is required under the pairwise union rule. Applicability therefore varies by field; blocker counts are multi-label across fields, while missing and different values are mutually exclusive within each field. Percentages are conditional on each field's applicable-pair denominator.

**Table 6. Leading cross-paper blockers among applicable pairs.**

| Field | Applicable pairs | Missing in record | Different present values | Blocked pairs | Blocked share |
| --- | ---: | ---: | ---: | ---: | ---: |
| Metric definition reference | 13,873 | 13,712 | 155 | 13,867 | >99.9% |
| Algorithm identifier | 13,873 | 13,864 | 0 | 13,864 | 99.9% |
| Metric identifier | 13,873 | 13,856 | 5 | 13,861 | 99.9% |
| Metric unit | 13,873 | 10,842 | 2,999 | 13,841 | 99.8% |
| Implementation protocol identifier | 12,750 | 12,750 | 0 | 12,750 | 100.0% |
| Number of assets | 12,750 | 7,270 | 5,049 | 12,319 | 96.6% |
| Claim target detail | 13,843 | 1,329 | 9,569 | 10,898 | 78.7% |
| Claim target | 13,873 | 0 | 10,422 | 10,422 | 75.1% |
| Result basis | 13,873 | 0 | 9,324 | 9,324 | 67.2% |
| Evaluation design | 13,873 | 0 | 9,176 | 9,176 | 66.1% |
| Comparator protocol identifier | 8,518 | 8,518 | 0 | 8,518 | 100.0% |
| Comparator method identifier | 8,518 | 8,511 | 0 | 8,511 | 99.9% |

![FIGURE:Figure 2](figures/Figure_2_blocker_composition.png)
**Figure 2. Cross-paper blocker composition among applicable pairs.** Bars partition each field’s applicable pairs into missing, different-present and unblocked values. Denominators vary by field; counts are descriptive.

At paper level, the three canonical-identifier blockers and metric-definition blocker each occurred in claim pairs involving all 756 paper pairs and all 56 papers. This can coexist with macro-target survival for every paper pair because the surviving and blocked claim pairs need not be the same.

The blocker taxonomy separates three actionable cases: recorded differences that define where non-pooling is appropriate, representation gaps that call for better mappings, and missing values that motivate closer attention to source reporting. Pair-level records distinguish known differences from missing values; attributing missingness to source reporting requires direct source review.

The five final survivors make the boundary concrete: pairs that align at the method/metric tier can still differ in contract family or maturity and lack comparator, calibration, dynamics, payoff, algorithm or implementation details. The complete residual table is retained in Supplement S3.

### 5.4 Prospective reconstruction and sensitivity

All twelve selected cases were sourced. Three isolated annotation contexts reviewed 96 field slots across 36 verified tasks. Independent masks made 93 slots eligible for overlay, and the review produced 44 scalar assignments: 20 updated stored values and 24 reassigned unchanged. Four final versions received the fixed audit. Composite values remained intact; 41 slots retained multi-valued lists, 8 remained unresolved and 3 were excluded.

The reconstruction included lexical, classification and assertion-scope differences as well as unchanged reassignments; two source-local metric definitions were retained without promotion to global identifiers. The 30 pilot pairs comprised six same-target and 24 different-target pairings. Original records yielded 29 incomparable and 1 insufficient-information verdict under each contract; reconstructed records yielded 30 incomparable verdicts under L0, T1 and I1. No pair was comparable in this source-anchored sample. The follow-up shows how source-based field reconstruction clarifies recorded comparison blockers across the selected strata.

Across the full 13,873 cross-paper pairs on original records, L0 assigned 13,792 incomparable and 81 insufficient-information verdicts; T1 assigned 13,813 and 60; I1 assigned 13,829 and 44. None of the three contracts classified a cross-paper pair as comparable. Pairwise transitions among the contracts were limited to the incomparable and insufficient-information classes: 71 pairs changed between L0 and T1, 59 between L0 and I1, and 16 between T1 and I1. No transition produced a comparable pair. These purpose-specific transitions reflect each contract's required fields and precedence rule, rather than a nested scale of comparability (Supplement S11).

Thirty-three synthetic controls passed all 99 contract-specific checks, including prespecified positive, mismatch and unknown cases. A worked source pair illustrates the value of separating these outcomes. Under T1, reconstructing its result basis changed the verdict from insufficient information to incomparable because the two claims used different result bases.

Full pair-path availability, source-review decisions, the historical cross-model diagnostic and the paired contract-transition audit are reported in Supplements S5, S6 and S11. Together, these materials report source-supported reconstructions alongside the field-level rules and operational outcomes of each comparison purpose.

### 5.5 Benchmark-assessability as a secondary diagnostic

Benchmark-assessability (BA) provides a complementary profile of the availability of ten claim fields. For each claim, it is calculated as:

\[
\operatorname{BA}(c)
=
\frac{\displaystyle\sum_{f \in A(c)} w_f I_f(c)}{\displaystyle\sum_{f \in A(c)} w_f}.
\]

The numerator sums the prespecified weights for applicable fields that are present after normalization; the denominator sums the weights for all applicable fields. Presence is syntactic and does not establish semantic correctness. Field weights, applicability and normalization rules are detailed in Supplement S4. With prespecified weights, the mean was 0.8418 overall, 0.8345 in F1 and 0.8491 in F2; the equal-weight mean was 0.8274 overall. Observed ranges were 0.4651-1.0000 in F1 and 0.6818-1.0000 in F2.

BA captures a defined set of reporting fields and complements the stricter direct-effect analysis. It is interpreted as a field-availability profile alongside its applicability rules, not as a substitute for claim comparability.

## 6. Reporting Recommendations for Benchmark-Ready Studies

Reporting should make comparison status assessable for the intended purpose without forcing distinct studies into one benchmark. Missing project-specific identifiers in historical records should not be treated as information that earlier authors were obliged to provide.

**Table 7. Recommended claim-level reporting information by category.**

| Category | Recommended claim-level information |
| --- | --- |
| Claim semantics | Application, target, target detail and direction |
| Method context | Algorithm surface and mapping status; computational model; backend; shots or reads where applicable |
| Evaluation context | Result basis, design, data or instance generator, mitigation, run protocol and implementation identifier |
| Metric semantics | Name, mapping status, unit, explicit definition, direction and reported uncertainty |
| Baseline | Comparator, method and protocol identifiers, implementation assumptions and threshold where relevant |
| Cost and scale | Cost boundary, assets, qubits, scenarios, paths, time steps and repetitions |
| Evidence | Source location and exact table, figure, equation or text provenance |

Portfolio studies should additionally report asset universe, data source, region, currency, objective, constraints, transaction costs, temporal protocol, rebalancing and baseline portfolio. Pricing studies should report contract and exercise style, payoff, underlying, dynamics, pricing measure, calibration, maturity, moneyness, discretization and target error. Existing ontology identifiers should be used only when semantics match uniquely; otherwise a documented local identifier should retain its definition, version, evidence and unresolved mapping status.

These fields do not prescribe one formulation, method or device. They expose the conditions under which an effect may be compared. A scientifically useful study may legitimately remain outside another study's direct-effect class. The framework therefore supports both justified alignment and explicit non-pooling.

Reporting should also distinguish literal source values, normalized surfaces and canonical mappings. Authors can assist reuse by giving versioned definitions and machine-readable identifiers, but repositories and reviewers should preserve unresolved status when a mapping is ambiguous. For continuous parameters, point estimates, grids and scaling curves should be labeled as different comparison objects. For costs, included and excluded components should be explicit. For baselines, both the method and the executed protocol should be identifiable, since a strong name does not guarantee an equivalent implementation.

## 7. Discussion

The funnel shows that topical connections are widespread, while claim pairs meeting progressively more specific comparison conditions become uncommon. Nearly one quarter of cross-paper pairs share a macro target, five meet the applicable method/metric tier, and none meets L0. Each stage has an inspectable meaning, so the result identifies where synthesis is supported and where it requires a different comparison purpose or additional evidence.

The blocker profiles reveal two complementary features of the evidence base. Many pairs contain at least one recorded difference in target, design, result basis, unit, scale or derivative context. In contrast, other pairs lack information needed to determine alignment in the absence of such a difference. Canonical algorithm and metric identifiers are sparse in the resolved records, reflecting the pilot registry's limited coverage as well as any source-level reporting; their absence alone should not be interpreted as evidence that a paper did not describe its method or metric. In the post-hoc sensitivity, omitting all L0 paths ending in `_id` or `_ref` still left no blocker-free pair. Identifier coverage therefore contributes to the observed blocker profile but does not, by itself, account for the strict zero. The full results separate these patterns from recorded differences in other comparison dimensions.

The practical contribution is a decision structure for evidence synthesis: define the comparison purpose, specify required fields, distinguish recorded differences from missing information, preserve source provenance and document reasons for pooling or non-pooling. Reusable crosswalks can pair source-local labels with candidate canonical identifiers, mapping evidence, mapping status and independent review. The current analysis applies unique normalized label or alias matches; future studies can test broader mappings and less restrictive contracts against independently selected positive, negative and boundary cases, with mappings and conversions fixed before outcomes are inspected. T1 and I1 provide explicit alternative purposes for this evaluation. By making comparison purposes and blockers visible, the framework supports justified alignment while preserving methodological diversity.

## 8. Threats to Validity

### 8.1 Internal and construct validity

Source-span and schema checks assess traceability and structural conformity. The fixed-sample review reports conditional consistency judgments, while the prospective source-anchored follow-up records field reconstruction, deterministic evidence checks, anonymized adjudication and a fixed-case audit. These results are reported descriptively; no chance-corrected reliability coefficient is inferred [56].

L0 uses exact stored-value equality, registry coverage and target-specific applicability. It may exclude scientifically defensible comparisons involving different algorithms, convertible units, overlapping grids or curves; matching explicit `unstated` values may also overstate alignment. T1 and I1 encode different purposes but retain exact metric, unit and definition requirements. Synthetic controls test the specified software rules; they do not establish that those rules capture every scientifically defensible comparison. BA summarizes a separate set of metadata fields and should be interpreted alongside its applicability rules. Testing tolerances, conversions or broader semantic mappings requires a separately specified evaluation with independently selected positive, negative and boundary cases.

### 8.2 External validity and dependence

The study focuses on two major financial application families, portfolio optimization and derivative pricing, enabling detailed claim-level analysis within a clearly defined scope. Source configurations, dated expansion-query records and the itemized corpus register document the discovery design and analyzed evidence base. Preprints and journal articles were both eligible. Pair counts share papers, methods, families and extraction waves; the analysis uses them to describe the structure of the audited evidence network.

### 8.3 Reproducibility

Frozen records and deterministic aggregates are content-addressed and rerunnable. AI-assisted structured claim-extraction and candidate-generation outputs are not guaranteed to be byte-identical across runs. Available telemetry identifies requested aliases but not runtime-model or provider identities; accordingly, the study does not compare model diversity, provider independence or compute efficiency. Reproducibility boundaries are summarized in Supplement S7.

## 9. Conclusion

Across 56 portfolio-optimization and derivative-pricing papers, 240 source-verified claims generated 13,873 cross-paper pairs. The evidence-alignment funnel identified 3,451 macro-target pairs, 510 core claim/design pairs and 5 method/metric pairs; none met the predefined L0 direct-effect contract. Pair diagnostics distinguish stored-value differences from missing information, revealing why topical overlap alone is insufficient for effect-level synthesis. In a source-anchored follow-up, 20 stored values changed and 24 were reassigned unchanged across twelve cases; no pair met any of the three operational contracts in the 30-pair pilot. Together, these findings provide a practical framework for stating comparison purposes, tracing blockers and identifying where better mappings or reporting can strengthen cumulative evidence. By turning comparison criteria into explicit, auditable relations, the framework provides a basis for cumulative synthesis that preserves methodological diversity while clarifying the conditions for comparison.

## Declarations

### Availability of data and materials

The supplementary methods and evidence, itemized corpus register and supplementary figures are included as Additional files 1 to 4. The reproducibility code, frozen analysis inputs and manuscript source corresponding to this version are publicly available in the FinancialQML reproducibility repository (https://github.com/rtales/FinancialQML-reproducibility/tree/v1.0.1), release v1.0.1. The structured research-data archive and itemized corpus register are available from Zenodo (https://doi.org/10.5281/zenodo.23811821). Full-text source publications are not redistributed; source-dependent reproduction requires lawful access to the cited editions.

### Use of generative AI and AI-assisted technologies

Large language models assisted with structured claim extraction and candidate generation.

## Additional files

**Additional file 1.** `Additional_file_1_Supplementary_Methods_and_Evidence.txt`. Supplementary methods, operational definitions, full diagnostic tables and follow-up evidence (Sections S1-S11).

**Additional file 2.** `Additional_file_2_Corpus_Bibliography.csv`. Itemized register of the 56 corpus papers, including family, paper identifiers and accepted-claim counts.

**Additional file 3.** `Additional_file_3_Figure_S1_contract_transitions.png`. Supplementary pairwise verdict-transition matrices for L0, T1 and I1.

**Additional file 4.** `Additional_file_4_Figure_S2_BA_distribution.png`. Supplementary empirical cumulative distributions of benchmark-assessability scores.

## List of abbreviations

F1, portfolio-optimization family; F2, derivative-pricing family; I1, implementation-aligned comparison contract; L0, strict record-level alignment contract; QML, quantum machine learning; QC, quantum computing; T1, task-and-outcome comparison contract.

## References

1. Egger DJ, Gambella C, Marecek J, et al. Quantum computing for finance: state-of-the-art and future prospects. IEEE Trans Quantum Eng. 2020;1:1-24. doi:10.1109/TQE.2020.3030314.
2. Orús R, Mugel S, Lizaso E. Quantum computing for finance: overview and prospects. Rev Phys. 2019;4:100028. doi:10.1016/j.revip.2019.100028.
3. Rebentrost P, Gupt B, Bromley TR. Quantum computational finance: Monte Carlo pricing of financial derivatives. Phys Rev A. 2018;98:022321. doi:10.1103/PhysRevA.98.022321.
4. Woerner S, Egger DJ. Quantum risk analysis. npj Quantum Inf. 2019;5:15. doi:10.1038/s41534-019-0130-6.
5. Stamatopoulos N, Egger DJ, Sun Y, et al. Option pricing using quantum computers. Quantum. 2020;4:291. doi:10.22331/q-2020-07-06-291.
6. Albareti FD, Ankenbrand T, Bieri D, et al. A structured survey of quantum computing for the financial industry. arXiv:2204.10026. 2022. doi:10.48550/arXiv.2204.10026.
7. Herman D, Googin C, Liu X, et al. Quantum computing for finance. Nat Rev Phys. 2023;5:450-465. doi:10.1038/s42254-023-00603-1.
8. Naik AS, Yeniaras E, Hellstern G, Prasad G, Vishwakarma SKLP. From portfolio optimization to quantum blockchain and security: a systematic review of quantum computing in finance. Financ Innov. 2025;11:88. doi:10.1186/s40854-025-00751-6.
9. Muzzioli S, Raheem F, Ferrara M, Giudici P, Siciliano R. Quantum computing in finance: a literature review and future directions for trustworthy financial AI. Front Artif Intell. 2026;9:1929828. doi:10.3389/frai.2026.1929828.
10. Markowitz H. Portfolio selection. J Finance. 1952;7:77-91. doi:10.1111/j.1540-6261.1952.tb01525.x.
11. Black F, Scholes M. The pricing of options and corporate liabilities. J Polit Econ. 1973;81:637-654. doi:10.1086/260062.
12. Glasserman P. Monte Carlo methods in financial engineering. New York: Springer; 2003. doi:10.1007/978-0-387-21617-1.
13. Rosenberg G, Haghnegahdar P, Goddard P, Carr P, Wu K, López de Prado M. Solving the optimal trading trajectory problem using a quantum annealer. IEEE J Sel Top Signal Process. 2016;10:1053-1060. doi:10.1109/JSTSP.2016.2574703.
14. Mugel S, Kuchkovsky C, Sanchez E, et al. Dynamic portfolio optimization with real datasets using quantum processors and quantum-inspired tensor networks. Phys Rev Res. 2022;4:013006. doi:10.1103/PhysRevResearch.4.013006.
15. Carrascal G, Hernamperez P, Botella G, del Barrio A. Backtesting quantum computing algorithms for portfolio optimization. IEEE Trans Quantum Eng. 2024;5(3):3100220. doi:10.1109/TQE.2023.3337328.
16. Grant E, Humble TS, Stump B. Benchmarking quantum annealing controls with portfolio optimization. Phys Rev Appl. 2021;15:014012. doi:10.1103/PhysRevApplied.15.014012.
17. Brandhofer S, Braun D, Dehn V, et al. Benchmarking the performance of portfolio optimization with QAOA. Quantum Inf Process. 2023;22:25. doi:10.1007/s11128-022-03766-5.
18. Buonaiuto G, Gargiulo F, De Pietro G, Esposito M, Pota M. Best practices for portfolio optimization by quantum computing, experimented on real quantum devices. Sci Rep. 2023;13:19434. doi:10.1038/s41598-023-45392-w.
19. Longstaff FA, Schwartz ES. Valuing American options by simulation: a simple least-squares approach. Rev Financ Stud. 2001;14:113-147. doi:10.1093/rfs/14.1.113.
20. Miyamoto K. Bermudan option pricing by quantum amplitude estimation and Chebyshev interpolation. EPJ Quantum Technol. 2022;9:3. doi:10.1140/epjqt/s40507-022-00124-3.
21. Kaneko K, Miyamoto K, Takeda N, Yoshino K. Quantum pricing with a smile: implementation of local volatility model on quantum computer. EPJ Quantum Technol. 2022;9:7. doi:10.1140/epjqt/s40507-022-00125-2.
22. Ramos-Calderer S, Pérez-Salinas A, García-Martín D, et al. Quantum unary approach to option pricing. Phys Rev A. 2021;103:032414. doi:10.1103/PhysRevA.103.032414.
23. Manzano A, Ferro G, Leitao Á, Vázquez C, Gómez A. Alternative pipeline for option pricing using quantum computers. EPJ Quantum Technol. 2025;12:28. doi:10.1140/epjqt/s40507-025-00328-3.
24. Montanaro A. Quantum speedup of Monte Carlo methods. Proc Math Phys Eng Sci. 2015;471:20150301. doi:10.1098/rspa.2015.0301.
25. Suzuki Y, Uno S, Raymond R, Tanaka T, Onodera T, Yamamoto N. Amplitude estimation without phase estimation. Quantum Inf Process. 2020;19:75. doi:10.1007/s11128-019-2565-2.
26. Grinko D, Gacon J, Zoufal C, Woerner S. Iterative quantum amplitude estimation. npj Quantum Inf. 2021;7:52. doi:10.1038/s41534-021-00379-1.
27. Manzano A, Musso D, Leitao Á. Real quantum amplitude estimation. EPJ Quantum Technol. 2023;10:2. doi:10.1140/epjqt/s40507-023-00159-0.
28. Chakrabarti S, Krishnakumar R, Mazzola G, Stamatopoulos N, Woerner S, Zeng WJ. A threshold for quantum advantage in derivative pricing. Quantum. 2021;5:463. doi:10.22331/q-2021-06-01-463.
29. Miyamoto K. On the bias in iterative quantum amplitude estimation. EPJ Quantum Technol. 2024;11:42. doi:10.1140/epjqt/s40507-024-00253-x.
30. Mitchell M, Wu S, Zaldivar A, et al. Model cards for model reporting. In: Proceedings of FAT*; 2019. p. 220-229. doi:10.1145/3287560.3287596.
31. Gebru T, Morgenstern J, Vecchione B, et al. Datasheets for datasets. Commun ACM. 2021;64:86-92. doi:10.1145/3458723.
32. Kitchenham B, Charters S. Guidelines for performing systematic literature reviews in software engineering. EBSE Technical Report EBSE-2007-01; 2007.
33. Petersen K, Feldt R, Mujtaba S, Mattsson M. Systematic mapping studies in software engineering. In: Proceedings of EASE; 2008. p. 68-77. doi:10.14236/ewic/EASE2008.8.
34. Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71. doi:10.1136/bmj.n71.
35. Wilkinson MD, Dumontier M, Aalbersberg IJ, et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci Data. 2016;3:160018. doi:10.1038/sdata.2016.18.
36. Pineau J, Vincent-Lamarre P, Sinha K, et al. Improving reproducibility in machine learning research. J Mach Learn Res. 2021;22(164):1-20. Available from: https://jmlr.org/papers/v22/20-303.html.
37. Jaradeh MY, Oelen A, Farfar KE, et al. Open Research Knowledge Graph: next generation infrastructure for semantic scholarly knowledge. arXiv:1901.10816. 2019. doi:10.48550/arXiv.1901.10816.
38. Wadden D, Lin S, Lo K, Wang LL, van Zuylen M, Cohan A, Hajishirzi H. Fact or fiction: verifying scientific claims. In: Proceedings of EMNLP; 2020. p. 7534-7550. doi:10.18653/v1/2020.emnlp-main.609.
39. DeYoung J, Jain S, Rajani NF, et al. ERASER: a benchmark to evaluate rationalized NLP models. In: Proceedings of ACL; 2020. p. 4443-4458. doi:10.18653/v1/2020.acl-main.408.
40. Rethlefsen ML, Kirtley S, Waffenschmidt S, et al. PRISMA-S: an extension to the PRISMA statement for reporting literature searches in systematic reviews. Syst Rev. 2021;10:39. doi:10.1186/s13643-020-01542-z.
41. Campbell M, McKenzie JE, Sowden A, et al. Synthesis without meta-analysis (SWiM) in systematic reviews: reporting guideline. BMJ. 2020;368:l6890. doi:10.1136/bmj.l6890.
42. van Deventer O, et al. Towards European standards for quantum technologies. EPJ Quantum Technol. 2022;9:33. doi:10.1140/epjqt/s40507-022-00150-1.
43. Thé JVG, Fraser RA, Rosas-Bustos J. Quantum computing and quantum machine learning for engineers and developers. Cham: Springer; 2025. doi:10.1007/978-3-031-98245-3.
44. Koch T, Bernal Neira DE, Chen Y, et al. The Quantum Optimization Benchmarking Library. Nat Comput Sci. 2026;6:653-671. doi:10.1038/s43588-026-00991-1.
45. Lorenz JM, Monz T, Eisert J, et al. Systematic benchmarking of quantum computers: status and recommendations. arXiv:2503.04905. 2025. doi:10.48550/arXiv.2503.04905.
46. Tomesh T, Gokhale P, Omole V, et al. SupermarQ: a scalable quantum benchmark suite. In: 2022 IEEE International Symposium on High-Performance Computer Architecture; 2022. p. 587-603. doi:10.1109/HPCA53966.2022.00050.
47. Bowles J, Ahmed S, Schuld M. Better than classical? The subtle art of benchmarking quantum machine learning models. arXiv:2403.07059. 2024. doi:10.48550/arXiv.2403.07059.
48. Lubinski T, Johri S, Varosy P, et al. Application-oriented performance benchmarks for quantum computing. IEEE Trans Quantum Eng. 2023;4:1-32. doi:10.1109/TQE.2023.3253761.
49. Rønnow TF, Wang Z, Job J, et al. Defining and detecting quantum speedup. Science. 2014;345(6195):420-424. doi:10.1126/science.1252319.
50. Eisert J, Hangleiter D, Walk N, et al. Quantum certification and benchmarking. Nat Rev Phys. 2020;2:382-390. doi:10.1038/s42254-020-0186-4.
51. Proctor T, Rudinger K, Young K, Nielsen E, Blume-Kohout R. Measuring the capabilities of quantum computers. Nat Phys. 2022;18:75-79. doi:10.1038/s41567-021-01409-7.
52. Bravo-Montes JA, Bastante M, Botella G, del Barrio A, García-Herrero F. A methodology to select and adjust quantum noise models through emulators: benchmarking against real backends. EPJ Quantum Technol. 2024;11:71. doi:10.1140/epjqt/s40507-024-00284-4.
53. Schuld M, Killoran N. Is quantum advantage the right goal for quantum machine learning? PRX Quantum. 2022;3:030101. doi:10.1103/PRXQuantum.3.030101.
54. Stopfer E, Wagner F. Quantum portfolio optimization: an extensive benchmark. arXiv:2509.17876. 2025. doi:10.48550/arXiv.2509.17876.
55. Ye B, Liang P, Sabzevari MT, Khan AA. Auditing empirical comparisons in quantum software. arXiv:2607.00516. 2026. doi:10.48550/arXiv.2607.00516.
56. Artstein R, Poesio M. Inter-coder agreement for computational linguistics. Comput Linguist. 2008;34:555-596. doi:10.1162/coli.07-034-R2.
