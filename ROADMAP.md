# 🗺️ AI and Machine Learning Roadmap

This roadmap records possible improvements, not completed functionality or delivery commitments.

## Priority 1: Reproducible environments

- [ ] Inspect all imports and create a verified dependency manifest.
- [ ] Pin compatible Python and package versions.
- [ ] Add clear per-notebook environment guidance if dependencies differ.
- [ ] Record seeds and dataset versions.

## Priority 2: Dataset governance

- [ ] Document exact source, version, licence, and checksum for each CSV.
- [ ] Add data dictionaries for each target and feature.
- [ ] Decide whether data may be redistributed.
- [ ] Add safe local data-path configuration.
- [ ] Remove absolute machine-specific paths.

## Priority 3: Methodology

- [ ] Review preprocessing order for leakage.
- [ ] Use Pipeline and ColumnTransformer where useful.
- [ ] Add stratified validation for classification when appropriate.
- [ ] Use time-aware splits for temporal financial data.
- [ ] Explain target definitions and class imbalance.
- [ ] Compare models with appropriate baselines.

## Priority 4: Evaluation and responsible AI

- [ ] Add confusion matrices and class-level metrics.
- [ ] Add residual analysis for regression.
- [ ] Document calibration and threshold choices where relevant.
- [ ] Expand healthcare limitations and bias discussion.
- [ ] Record model limitations and intended-use boundaries.

## Priority 5: Automation and maintenance

- [ ] Validate notebook structure in CI.
- [ ] Add safe notebook execution checks when datasets are available.
- [ ] Clear stale outputs and sensitive notebook metadata.
- [ ] Keep documentation synchronized with active notebook cells.
