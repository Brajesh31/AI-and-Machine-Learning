# 📜 Changelog

This file records meaningful verified repository changes. Planned work belongs in ROADMAP.md.

## [Unreleased]

### Added
- Expanded project README with notebook catalogue, dataset requirements, methodology, evaluation, and responsible-use boundaries.
- Added technical guides for datasets, methodology, metrics, reproducibility, and responsible AI.
- Added a documentation index and maintainer/governance guidance.
- Added CI for notebook structure, Python cell syntax, and repository tests.
- Added runtime and development dependency manifests, a dataset manifest, a static notebook validator, and repository integrity tests.
- Corrected the regression notebook's inline package-install cell, the diabetes BMI category ordering, and the liver notebook's SVM scaling path.
- Removed the hourly README timestamp workflow to prevent unnecessary automated commits.
- Added ignore rules for Python caches, notebooks checkpoints, virtual environments, and private local data.

### Clarified
- The repository contains four notebooks and does not include the CSV files referenced by the notebooks.
- Healthcare examples are educational and are not clinically validated.
- Dependency ranges are provided, but a fully locked environment is not yet available.
- The CSV datasets remain external pending source and redistribution verification.

## Changelog maintenance

For future updates, record user-visible notebook changes, methodological improvements, documentation, reproducibility, and security work. Include dates and release versions only when a real release is created. Never claim experiments were re-run unless they were executed with documented data and environment versions.
