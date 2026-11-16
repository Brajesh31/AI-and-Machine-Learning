# Dataset directory

The notebooks expect external CSV datasets. They are intentionally not included here because their source, redistribution licence, provenance, and suitability for public redistribution have not been verified.

## Expected files

| Notebook | Expected CSV | Current status |
|---|---|---|
| Liver Disease Prediction | `liver_cirrhosis.csv` | Not included |
| Data Preprocessing and Regression | `LoansData (1).csv` | Not included |
| Naive Bayes Healthcare | `diabetes.csv` | Not included |
| Random Forest | `Cryptocurrency_FeaturedData.csv` | Not included |

Obtain each dataset from its legitimate publisher and review its licence before use. Put the CSV in the repository root for the current notebook paths, or update the notebook to use a configurable path under `data/`.

Do not commit patient data, private records, credentials, restricted data, or datasets whose licence prohibits redistribution. Do not use fabricated or synthetic data as a substitute while reporting results from the original dataset.

For each dataset, document its source URL, version or retrieval date, licence, checksum where practical, row/column count, target definition, and known limitations. See [Dataset Governance](../docs/data-governance.md).
