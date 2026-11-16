# 🧰 Maintainer Guide

## Responsibilities

Maintain the educational purpose of the notebook collection, keep data and modelling claims accurate, review changes for privacy and methodology, and preserve reproducibility where possible.

## Issue triage

Classify reports as notebook defects, data access issues, environment problems, modelling/evaluation concerns, documentation errors, security reports, or feature proposals. Request sanitized reproduction details and never ask for private patient records.

## Notebook review

For every material change:
- Identify the target and feature set.
- Confirm source and licence of the dataset.
- Check train/test splitting and preprocessing order.
- Look for leakage from target or future information.
- Review missing-value and outlier assumptions.
- Verify metric choice and class balance.
- Inspect outputs for private information and stale results.
- Run from a clean kernel where data and environment are available.
- Record Python and package versions.

## Healthcare review

Healthcare examples must be described as educational. Do not approve claims that a notebook is clinically valid without independent evidence, domain review, and appropriate governance. Never expose identifiable health data.

## Dependency maintenance

Add only dependencies actually used. Pin compatible versions after verifying the notebooks in a clean environment. Keep the dependency file and environment instructions synchronized.

## Release preparation

1. Review notebook diffs, including hidden cell outputs and metadata.
2. Confirm dataset provenance and access rights.
3. Run affected notebooks from clean kernels when possible.
4. Document unavailable external datasets or blocked execution.
5. Update README and CHANGELOG.
6. Review responsible-use statements.
7. Check no private data or credentials are included.
8. Tag a release only when an actual release is prepared.

## Repository hygiene

Avoid machine-specific paths, notebook checkpoints, IDE state, caches, huge raw datasets without licensing review, and generated model artifacts that are not intentionally versioned.

## Routine checklist

- [ ] Review open issues and pull requests.
- [ ] Check dependency advisories.
- [ ] Verify notebook links and documentation links.
- [ ] Review dataset assumptions.
- [ ] Check for leaked outputs and private data.
- [ ] Review modelling metrics and validation strategy.
- [ ] Update changelog for meaningful changes.
