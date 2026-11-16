# 🧪 Machine Learning Methodology

This guide describes a sound workflow for reviewing the repository's preprocessing and modelling notebooks. It distinguishes practices described by the notebook code from recommendations for more reliable experiments.

## 1. Understand the prediction task

Before fitting a model, identify:
- The unit represented by each row.
- The target column and its meaning.
- The prediction time and available information.
- Whether the task is regression or classification.
- Whether observations are independent or grouped/time-dependent.
- The practical cost of different prediction errors.

Do not infer a target's meaning from a short column name alone.

## 2. Inspect the raw data

Use descriptive statistics, column types, distributions, missingness summaries, and duplicate checks. Verify that numeric columns have actually been parsed as numeric and that categorical values have not silently become missing.

## 3. Split before fitting transformations

For predictive evaluation, split the data before fitting scalers, imputers, encoders, feature selectors, or outlier thresholds. Fit each transformation on training data only. Apply the fitted transformation unchanged to validation and test data.

A scikit-learn Pipeline or ColumnTransformer can make this boundary explicit and reduce leakage risk.

## 4. Handle missing and invalid values

Some healthcare measurements can use zero as a placeholder for an unavailable measurement. That assumption must be confirmed from the data dictionary. Do not convert all zero values to missing indiscriminately.

Document imputation strategy, per-feature missingness, and whether missingness itself may carry information.

## 5. Treat outliers carefully

IQR-based rules are useful exploratory tools but can remove valid rare observations. Define thresholds using training data only, inspect domain meaning, and compare results with and without the treatment.

## 6. Encode categorical features

One-hot encoding or dummy variables may be suitable for nominal categories. Avoid fitting encoders across the entire dataset before the split. Handle unseen categories in a defined way when building a reusable pipeline.

## 7. Scale features when appropriate

Distance-based models such as KNN are sensitive to feature scale. Tree-based estimators such as Random Forest generally do not require standardization for the same reason. Apply transformations based on model assumptions, not as an automatic step for every algorithm.

## 8. Train and tune

Separate model fitting from hyperparameter selection. Use cross-validation on training data. Keep the final test set untouched until model selection is complete. For time-dependent cryptocurrency data, consider chronological or walk-forward validation rather than random shuffling.

## 9. Evaluate and interpret

Use metrics appropriate to the task and class distribution. Inspect confusion matrices, class-level scores, residual plots, and errors. Avoid selecting a model solely because it has the highest accuracy.

## 10. Record the experiment

Record dataset provenance, split strategy, target definition, preprocessing steps, model parameters, random seed, package versions, metrics, and known limitations. Do not claim reproducibility without those details.

## Current notebook limitations

The notebooks are independent learning exercises and may not consistently implement all recommended safeguards. Review the active cells before treating any score as an unbiased estimate of generalization.
