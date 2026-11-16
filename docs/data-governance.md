# 🔐 Dataset Governance and Data Handling

This repository references external CSV datasets but does not currently distribute those files. Contributors are responsible for checking that any data they use or propose to add is lawful, appropriately licensed, and safe to share.

## 1. Before using a dataset

Record the following information before relying on a dataset:
- Dataset title and publisher.
- Canonical source URL or repository.
- Version, release date, or retrieval date.
- Licence and redistribution conditions.
- Collection methodology and population represented.
- Target and feature definitions.
- Known limitations, missingness, and sampling bias.
- Whether personal, sensitive, health, or confidential information is present.

A filename alone is not data provenance.

## 2. What must not be committed

Do not commit:
- Patient records or identifiable health information.
- Personal information without a valid legal basis and explicit authorization.
- Credentials, access tokens, private keys, or database connection strings.
- Confidential, proprietary, or restricted datasets.
- Data whose licence prohibits redistribution.
- Raw exports containing hidden identifiers or sensitive notebook outputs.

Use synthetic or appropriately anonymized examples for demonstrations and issue reports. Anonymization must not be assumed merely because names have been removed.

## 3. Local dataset placement

Keep external datasets outside version control unless their redistribution is explicitly permitted and the repository maintainer approves their inclusion.

The notebooks currently refer to these filenames:
- `liver_cirrhosis.csv`
- `diabetes.csv`
- `Cryptocurrency_FeaturedData.csv`
- The regression notebook's exact CSV filename must be confirmed from its cells.

Place files where the notebook expects them, or update the notebook to use a documented configurable data path. Do not upload private datasets to make CI pass.

## 4. Data quality and leakage

Before training:
1. Inspect schema and data types.
2. Validate target labels and feature meaning.
3. Check duplicates and invalid values.
4. Inspect class imbalance and missingness.
5. Identify identifiers and target-derived features.
6. Split data before fitting preprocessing transformations.
7. Fit preprocessing only on training data.
8. Keep the final test set isolated until final evaluation.

Outlier thresholds, imputers, scalers, encoders, and feature-selection rules can leak information when calculated on the full dataset before splitting.

## 5. Healthcare data safeguards

Health-related data is especially sensitive. Do not use real patient records in public issues, pull requests, screenshots, notebook outputs, or commits. Educational healthcare datasets do not automatically represent clinical populations or support clinical conclusions.

Any proposal to include health data requires documented provenance, legal and ethical review, a clear purpose, privacy safeguards, and maintainer approval before the data is added.

## 6. Dataset change record

When a dataset source, version, or schema changes, update the dataset documentation and explain:
- What changed and why.
- Whether the target definition changed.
- Whether rows, features, or population coverage changed.
- Whether previous results remain comparable.
- Whether experiments were rerun.
- Whether model cards and limitations need revision.

## 7. Incident response

If sensitive data or credentials are committed:
1. Stop sharing the affected artifact.
2. Notify the repository maintainer through the private reporting channel in `SECURITY.md`.
3. Revoke and rotate exposed credentials immediately.
4. Remove the data from active repository history as coordinated with the maintainer.
5. Assess forks, caches, artifacts, and other copies.
6. Do not reproduce the sensitive content in an issue or public discussion.

Deleting a file in a later commit does not erase it from Git history.
