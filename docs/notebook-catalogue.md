# 📒 Notebook Catalogue

This document inventories the four notebooks in the repository and records their visible data dependencies and modelling topics. It is intended as a guide for exploration, not a substitute for reading the notebook cells.

## 1. Data Preprocessing and Regression

**Notebook:** `Mini Project - Data Preprocessing & Regression Model.ipynb`

The README describes an end-to-end preprocessing and OLS regression exercise. The documented topics include missing-value treatment, duplicate inspection, IQR outlier handling, categorical encoding, scaling, feature engineering, train/test splitting, and OLS evaluation.

**Libraries named in project documentation:** Pandas, NumPy, Matplotlib, Seaborn, scikit-learn, Statsmodels.

**Data dependency:** `LoansData (1).csv`, not included in the repository.

**Review before trusting metrics:** check that train/test separation occurs before learning preprocessing parameters, that transformations do not use target information, and that residual and error metrics are interpreted correctly.

## 2. Liver Disease Classification

**Notebook:** `Liver Disease Prediction (KNN , Desicion Tree , Naive Bayes).ipynb`

**Observed input:** `liver_cirrhosis.csv`.

The current code trains K-Nearest Neighbors, Decision Tree, Logistic Regression, and Support Vector Machine classifiers. The filename includes Naive Bayes, but no Naive Bayes estimator is implemented in the current notebook. The `Report_curable` target is derived from the source dataset's Stage field and is not a clinical determination. The binary classification workflow now uses LogisticRegression rather than treating the binary target as an OLS regression problem.

## 3. Diabetes Naive Bayes Classification

**Notebook:** `Mini project (Naive Bayes Healthcare dataset).ipynb`

**Observed input:** `diabetes.csv`.

The notebook imports GaussianNB and BernoulliNB. It creates glucose, BMI, and age categories, applies dummy encoding, filters insulin observations using an IQR rule, applies a logarithmic transform to insulin, and a square-root transform to skin thickness. It does not currently implement zero-value imputation or feature scaling.

The code compares train and test accuracy. A more complete evaluation should also include class-wise precision, recall, F1-score, a confusion matrix, and validation of class proportions.

## 4. Cryptocurrency Random Forest Classification

**Notebook:** `Mini project (Random Forest).ipynb`

**Observed input:** `Cryptocurrency_FeaturedData.csv`.

The notebook imports RandomForestClassifier and GridSearchCV. Its parameter grid explores estimator count, tree depth, minimum samples for splitting and leaves, and the number of features considered. The search uses five-fold cross-validation and accuracy scoring. The final evaluation now uses `gscv_rf.best_estimator_` rather than fitting a separate model with unrelated hard-coded parameters.

Check the target definition and time ordering before interpreting a random split on cryptocurrency data. If observations are time-dependent, random splitting may lead to an optimistic estimate.

## Notebook inventory limitations

- The repository does not contain the CSV files named above.
- Notebook cells may retain stale output from previous executions.
- Execution counters and saved output are not proof of a fresh run.
- The notebooks do not share a common pipeline or package.
- CI validates notebook JSON structure and Python syntax in code cells. It does not execute model-training cells.

When a notebook changes materially, update this catalogue with verified details and record the environment and data provenance.
