# 🤝 Contributing to AI and Machine Learning

Thank you for helping improve this collection of educational machine-learning notebooks. Contributions should prioritize methodology, reproducibility, data provenance, responsible interpretation, and clear explanations.

## 📚 Table of Contents

- [Project scope](#-project-scope)
- [Ways to contribute](#-ways-to-contribute)
- [Before changing a notebook](#-before-changing-a-notebook)
- [Environment setup](#-environment-setup)
- [Notebook development standards](#-notebook-development-standards)
- [Machine-learning methodology](#-machine-learning-methodology)
- [Dataset and privacy rules](#-dataset-and-privacy-rules)
- [Healthcare-related contributions](#-healthcare-related-contributions)
- [Validation expectations](#-validation-expectations)
- [Pull request checklist](#-pull-request-checklist)

## 🎯 Project scope

This repository contains four independent Jupyter notebooks covering regression, data preprocessing, healthcare classification, Naive Bayes, KNN, Decision Trees, and Random Forest. It is not a packaged ML platform or production model service.

Keep proposed changes relevant to the learning goals. A new framework, API, database, or deployment platform requires a clear use case and separate design.

## 💡 Ways to contribute

| Area | Useful contribution |
|---|---|
| Notebook clarity | Improve markdown explanations and variable naming |
| Data quality | Clarify missingness, duplicates, and target definitions |
| Methodology | Prevent leakage and improve validation |
| Evaluation | Add appropriate metrics and error analysis |
| Reproducibility | Record versions, random seeds, and data provenance |
| Responsible AI | Explain bias, privacy, and limitations |
| Documentation | Improve setup instructions and notebook catalogue |

## 🔎 Before changing a notebook

1. Read the notebook from the first cell to the last.
2. Identify the target variable and feature set.
3. Confirm the dataset source and licence.
4. Review the order of train/test splitting and preprocessing.
5. Identify whether the task is regression, binary classification, or multiclass classification.
6. Understand which metrics are appropriate.
7. Check whether saved outputs are stale or contain sensitive information.

## 🧪 Environment setup

Use a virtual environment and install the dependencies described in the repository README. The repository currently does not pin exact versions, so record Python and package versions when results change.

Start Jupyter from the repository root so that relative data paths behave predictably.

## 📓 Notebook development standards

- Use meaningful markdown headings.
- Explain why a preprocessing choice is made.
- Group imports and remove unused imports in the notebook being revised.
- Keep variables descriptive.
- Avoid absolute machine-specific paths.
- Set random seeds where supported.
- Run cells in order from a clean kernel.
- Do not leave misleading stale outputs.
- Keep outputs concise and inspect them for sensitive data.
- Prefer reusable scikit-learn pipelines when they improve clarity.
- Document assumptions rather than hiding them in code.

## 🧠 Machine-learning methodology

### Data splitting

Create training and test sets before fitting transformations that learn from data. Fit imputers, scalers, encoders, feature selectors, and outlier thresholds on training data only.

### Validation

Use cross-validation on the training data for model selection. Do not repeatedly tune using the final test set. Use stratification for classification when appropriate and chronological validation for time-dependent data.

### Metrics

Report metrics suited to the target and error costs. Include class-wise metrics and confusion matrices for imbalanced classification. For regression, explain the units and interpretation of errors.

### Reproducibility

Record dataset version, random seed, split method, preprocessing, model parameters, and library versions. Do not claim a result is reproducible when a required dataset or environment is unavailable.

## 📊 Dataset and privacy rules

- Confirm dataset source, licence, and redistribution conditions.
- Do not commit private or restricted data.
- Do not commit personally identifiable or patient data.
- Document required CSV filenames and expected paths.
- Use synthetic examples in issues and pull requests.
- Remove machine-specific paths and private notebook outputs.

## 🩺 Healthcare-related contributions

The liver and diabetes notebooks are educational examples. Contributions must not describe them as clinically validated or suitable for diagnosis, treatment, screening, or patient triage. Do not make unsupported claims about medical usefulness. Any real clinical use would require independent validation, domain expertise, privacy safeguards, governance, and applicable regulatory review.

## ✅ Validation expectations

Before submitting:
- Run the changed notebook from a clean kernel if the dataset is available.
- Record any cells that could not be executed and why.
- Validate notebook JSON structure.
- Review all outputs and metadata.
- Confirm no secrets or private data are present.
- Check that preprocessing is leakage-aware.
- Compare metrics on the correct split.
- Update documentation and changelog.

The current CI workflow validates notebook structure, not model correctness or full notebook execution.

## 📝 Pull request checklist

- [ ] The change has a clear educational or methodological purpose.
- [ ] Dataset source and licence are documented.
- [ ] No private data or credentials are included.
- [ ] The train/test boundary is respected.
- [ ] Metrics match the prediction task.
- [ ] Random seeds and package versions are recorded where relevant.
- [ ] The notebook runs from a clean kernel, or execution limitations are stated.
- [ ] Results are not overstated.
- [ ] Responsible-use documentation is updated.
- [ ] CHANGELOG.md is updated for meaningful changes.
