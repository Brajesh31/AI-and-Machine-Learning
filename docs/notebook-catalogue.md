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

The notebook imports KNeighborsClassifier, DecisionTreeClassifier, LogisticRegression, SVC, StandardScaler, train_test_split, GridSearchCV, and classification metrics. Evaluation code references a `Report_curable` target field.

The filename and historical README mention KNN, Decision Tree, and Naive Bayes, but imports alone do not prove every model is trained. Inspect executed cells before recording final model comparisons.

## 3. Diabetes Naive Bayes Classification

**Notebook:** `Mini project (Naive Bayes Healthcare dataset).ipynb`

**Observed input:** `diabetes.csv`.

The notebook imports GaussianNB and BernoulliNB. It contains handling for selected zero-valued measurements, median imputation, logarithmic and square-root feature transformations, age and BMI categories, dummy encoding, and scaling.

The code compares train and test accuracy. A more complete evaluation should also include class-wise precision, recall, F1-score, a confusion matrix, and validation of class proportions.

## 4. Cryptocurrency Random Forest Classification

**Notebook:** `Mini project (Random Forest).ipynb`

**Observed input:** `Cryptocurrency_FeaturedData.csv`.

The notebook imports RandomForestClassifier and GridSearchCV. Its parameter grid explores estimator count, tree depth, minimum samples for splitting and leaves, and the number of features considered. The search uses five-fold cross-validation and accuracy scoring.

Check the target definition and time ordering before interpreting a random split on cryptocurrency data. If observations are time-dependent, random splitting may lead to an optimistic estimate.

## Notebook inventory limitations

- The repository does not contain the CSV files named above.
- Notebook cells may retain stale output from previous executions.
- Execution counters and saved output are not proof of a fresh run.
- The notebooks do not share a common pipeline or package.
- No automated notebook execution workflow is currently present.

When a notebook changes materially, update this catalogue with verified details and record the environment and data provenance.
