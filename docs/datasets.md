# 📊 Dataset Requirements and Data Governance

The notebooks load CSV files from local relative paths. The repository tree currently contains the four notebooks but does not include the input CSV datasets. A notebook that refers to a filename does not imply that the file is distributed with this repository.

## Expected dataset files

| Notebook | CSV filename referenced or to verify | Repository status |
|---|---|---|
| Liver classification | `liver_cirrhosis.csv` | Not included |
| Diabetes Naive Bayes | `diabetes.csv` | Not included |
| Random Forest | `Cryptocurrency_FeaturedData.csv` | Not included |
| Preprocessing and OLS | Confirm exact filename from notebook cells | Not included in repository tree |

## Obtaining data responsibly

Before downloading or using a dataset:
1. Identify the original publisher.
2. Read the dataset's licence and terms.
3. Check whether redistribution is permitted.
4. Record the exact source URL and access date.
5. Record version, checksum, and any transformation performed.
6. Inspect field definitions and target-label meaning.
7. Avoid collecting data that is not necessary for the experiment.

Do not assume a dataset found under the same filename is the same version used in the original notebook.

## Local placement

Place an authorized CSV next to the notebook if the notebook expects a root-relative filename, or update the path deliberately in a separate code change. Start Jupyter from the repository root to make working-directory assumptions easier to reason about.

Do not commit large, private, restricted, or identifiable datasets without explicit permission and a clear legal basis.

## Healthcare data

The liver and diabetes experiments use health-related records or labels. Even de-identified data can carry re-identification risks. Do not upload real patient records, names, dates of birth, contact details, medical record numbers, or free-text notes to GitHub.

## Cryptocurrency dataset

Confirm the source, licence, observation timestamp, feature construction, target definition, and time period. Financial datasets can contain temporal dependence, survivorship effects, and leakage. A random train/test split is not necessarily suitable for time-dependent predictions.

## Data dictionary template

For future data additions, document:

| Field | Description |
|---|---|
| Dataset name | Exact dataset title |
| Source | Official publisher or repository |
| Version | Release/version/date |
| Licence | Permitted use and redistribution |
| Access date | Date obtained |
| Record count | Number of rows |
| Feature count | Number of predictor fields |
| Target | Exact target column and definition |
| Missingness | Missing values by field |
| Population/time range | Who or what is represented |
| Restrictions | Privacy, legal, or redistribution limits |

## Data removal and incident handling

If private or restricted data is committed, remove public exposure, restrict access, and contact the repository maintainer. If credentials are exposed, revoke them at the issuing service. Removing a file from the latest commit does not erase all history or make an exposure safe.
