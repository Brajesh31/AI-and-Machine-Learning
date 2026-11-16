# 📏 Model Evaluation Guide

Evaluation should communicate how a model behaves, not just provide a single score. The repository contains regression and classification examples, so metrics must be selected based on the task.

## Classification metrics

### Confusion matrix

For binary classification, the confusion matrix counts:
- True positives.
- True negatives.
- False positives.
- False negatives.

Always document which class is considered positive.

### Accuracy

The fraction of all predictions that are correct. Accuracy can be misleading when classes are imbalanced.

### Precision

Of the cases predicted positive, the proportion that are truly positive. Low precision means more false positives.

### Recall

Of the actual positive cases, the proportion detected by the model. Low recall means more false negatives.

### F1-score

The harmonic mean of precision and recall. It is useful when both matter, but it does not encode the business or clinical cost of an error.

### Additional reporting

Consider:
- Per-class precision, recall, and F1.
- Macro and weighted averages.
- Confusion matrix.
- ROC-AUC or PR-AUC where appropriate and correctly computed.
- Calibration, where predicted probabilities are used.
- Confidence intervals or repeated validation for stability.

For healthcare examples, do not treat one metric as evidence of clinical utility.

## Regression metrics

### Mean Absolute Error

Average absolute difference between predictions and observed values. It is expressed in the target's units.

### Mean Squared Error

Average squared error. It penalizes larger errors more strongly and is expressed in squared target units.

### Root Mean Squared Error

Square root of MSE, returned to the target's units.

### R-squared

A measure of variance explained relative to a baseline. It can be negative on held-out data and does not establish causality or model correctness.

## Train versus test

A strong training score paired with a much weaker test score may indicate overfitting, leakage, or distribution shift. Similar scores do not prove that the split is representative.

The test set must not be repeatedly used to tune a model. Model selection belongs inside training-only cross-validation.

## Model comparison template

| Model | Validation strategy | Metric | Score | Notes |
|---|---|---|---:|---|
| Baseline | To document | To define | Not recorded here | Establish reference |
| Candidate A | To document | To define | Not recorded here | Record parameters |
| Candidate B | To document | To define | Not recorded here | Record error profile |

No new model score is reported in this guide because the datasets were not available for a fresh, reproducible run.
