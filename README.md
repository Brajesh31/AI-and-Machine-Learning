 1) 📊 **Mini Project - Data Preprocessing & Regression Model**

---

### 📌 Introduction

This project focuses on end-to-end data preprocessing and regression model building. The main objective is to clean, transform, and prepare raw data for machine learning tasks, followed by implementing an **Ordinary Least Squares (OLS) Regression** model. It demonstrates important concepts of data cleaning, handling missing values, encoding categorical data, feature engineering, and model evaluation.

---

### 🚀 Features

* Handling missing values (numerical & categorical)
* Outlier detection and treatment using **IQR method**
* Encoding categorical features (**One-Hot Encoding**)
* Data transformation and standardization
* Feature engineering for better model performance
* Splitting dataset into training and testing
* Building and evaluating **OLS Regression models**

---

### 🛠️ Technology Used

* **Python**
* **Jupyter Notebook**
* **Libraries:**

  * Pandas
  * NumPy
  * Matplotlib / Seaborn (for visualization)
  * Scikit-learn
  * Statsmodels (for OLS Regression)

---

### 📂 How to Use

1. Clone or download the project notebook.
2. Install the required libraries:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
   ```
3. Open the notebook in Jupyter:

   ```bash
   jupyter notebook "Mini project 1.ipynb"
   ```
4. Run cells step by step to:

   * Preprocess data
   * Apply transformations
   * Train and evaluate the regression model

---

### 📖 Topics Covered

* **Data Cleaning & Preprocessing**

  * Handling duplicates
  * Missing value treatment (numerical & categorical)
  * Outlier detection (Boxplot, IQR method)
* **Data Transformation**

  * Standardization & Normalization
  * Feature engineering
* **Categorical Data Encoding**
* **Dataset Splitting (Train/Test)**
* **Model Building**

  * OLS Regression
  * Model evaluation (R², comparison between transformations)

---

### ✅ Conclusion

This project helps in understanding the workflow of **data preprocessing to model building**. By exploring multiple transformations and comparing their effects on regression accuracy, it provides **hands-on experience in preparing datasets for predictive modeling**.








 2) # 📊 Liver Disease Prediction - README

## 📌 Project Overview

This project focuses on predicting whether a liver disease case is **curable** or **not curable** based on patient medical data. The model is trained using different classification algorithms and evaluated using standard performance metrics.

## 🚀 Features

* Data preprocessing (cleaning, transformations, handling missing values)
* Implementation of multiple machine learning classification models:

  * Logistic Regression
  * Naive Bayes
  * Support Vector Machine (SVM)
  * K-Nearest Neighbors (KNN)
  * Decision Tree
  * Random Forest
* Model evaluation using:

  * Accuracy
  * Precision
  * Recall
  * F1 Score
* Performance comparison of algorithms

## 🛠️ Tech Stack

* **Language:** Python 🐍
* **Libraries:**

  * `pandas`, `numpy` → Data handling
  * `scikit-learn` → Machine Learning models & metrics
  * `matplotlib`, `seaborn` → Visualization

## 📂 Project Files

* `Predicted modeling on liver data (3).ipynb` → Main Jupyter Notebook with preprocessing, model building, and evaluation
* `README.md` → Project documentation (this file)

## 📊 Evaluation Metrics

The model is evaluated using the following:

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_train_class = (y_train_pred > 0.5).astype(int)

print("Accuracy :", accuracy_score(train["Report_curable"], y_train_class))
print("Precision:", precision_score(train["Report_curable"], y_train_class))
print("Recall   :", recall_score(train["Report_curable"], y_train_class))
print("F1 Score :", f1_score(train["Report_curable"], y_train_class))
```

## 📈 Possible Improvements

* Outlier treatment
* Feature engineering
* Hyperparameter tuning
* Using ensemble methods (XGBoost, Gradient Boosting)
* Cross-validation for robust evaluation

## 🎯 Goal

To build an accurate and reliable machine learning model that can help in early prediction and categorization of liver disease outcomes, assisting healthcare professionals in decision-making.

---

✍️ **Author:** Brajesh kumar




3) # Project: Random Forest Classification with Model Evaluation

## Overview

This project demonstrates the implementation of **Random Forest Classification** along with other machine learning models such as **K-Nearest Neighbors (KNN)** and **Decision Tree Classifier**. The dataset is preprocessed, trained, and evaluated using multiple metrics to assess model performance.

## Key Features

* Data Preprocessing (handling missing values, transformations, outlier treatment)
* Model Training using:

  * Random Forest Classifier
  * Decision Tree Classifier
  * K-Nearest Neighbors (KNN)
* Hyperparameter Tuning using **GridSearchCV**
* Model Evaluation using:

  * Accuracy
  * Precision
  * Recall
  * F1 Score

## Technologies Used

* Python 3
* Scikit-learn
* Pandas
* NumPy
* Jupyter Notebook

## Steps Performed

1. **Import Libraries**: Loaded required libraries for machine learning and evaluation.
2. **Data Preprocessing**: Cleaned and transformed dataset to prepare for model training.
3. **Model Building**:

   * Random Forest Classifier was trained with GridSearchCV for hyperparameter optimization.
   * Decision Tree and KNN were also implemented for comparison.
4. **Evaluation**:

   * Predictions compared with actual labels.
   * Performance evaluated using accuracy, precision, recall, and F1 score.

## Results

* The models were evaluated and compared.
* Random Forest generally provided higher performance compared to Decision Tree and KNN.

## How to Run

1. Install required libraries:

   ```bash
   pip install scikit-learn pandas numpy jupyter
   ```
2. Open the Jupyter Notebook:

   ```bash
   jupyter notebook "Mini project (Random Forest).ipynb"
   ```
3. Run cells step by step to see preprocessing, training, and evaluation results.

## Future Improvements

* Perform outlier treatment and feature transformation for better accuracy.
* Try additional models like **SVM, Logistic Regression, Gradient Boosting**.
* Implement feature importance visualization.

## Author

Brajesh 







4) # 📊 Naive Bayes on Healthcare Dataset

## 📌 Project Overview

This project applies **Naive Bayes classifiers** (GaussianNB & BernoulliNB) on a healthcare dataset (Diabetes Prediction). The aim is to classify patients as **diabetic or non-diabetic** based on various health parameters such as glucose, blood pressure, insulin, BMI, etc.

---

## ⚙️ Steps Performed

### 1. Data Preprocessing

* Loaded the diabetes dataset.
* Replaced invalid values (like 0 in Glucose, BloodPressure, Insulin, SkinThickness, BMI) with **NaN**.
* Imputed missing values using **median strategy**.
* Applied transformations to handle skewness:

  * `np.log1p()` for Insulin
  * `np.sqrt()` for SkinThickness
* Feature engineering:

  * Created bins for **Age Groups** (20-30, 30-40, 40-50, 50-60, 60+)
  * Created BMI categories (Underweight, Normal, Overweight, Obese)
* Converted categorical bins into dummy variables.
* Scaled numerical features using **StandardScaler**.

---

### 2. Model Training

Two models were trained and evaluated:

* **Gaussian Naive Bayes** → Suitable for continuous features.
* **Bernoulli Naive Bayes** → Suitable for binary features.

---

### 3. Model Evaluation

* Compared **Train Accuracy** and **Test Accuracy** of both models.
* Used metrics: **Accuracy, Precision, Recall, F1-score**.
* Observed class imbalance (500 non-diabetic, 268 diabetic cases) → considered in evaluation.

---

## 📈 Results

* **GaussianNB** generally performs better for this dataset since features are continuous.
* **BernoulliNB** can still be tested after binarizing features.
* Both models provide a good baseline for classification.

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy** (Data Handling)
* **Matplotlib, Seaborn** (EDA & Visualization)
* **Scikit-learn** (Modeling & Evaluation)

---

## 🚀 How to Run

1. Clone this repo:

   ```bash
   git clone <your-repo-link>
   ```
2. Navigate into the folder:

   ```bash
   cd naive-bayes-healthcare
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the notebook:

   ```bash
   jupyter notebook "Mini project (Naive Bayes Healthcare dataset).ipynb"
   ```

---

## 📌 Future Improvements

* Use **SMOTE** or class weights to handle imbalance.
* Try **Multinomial Naive Bayes** on discretized features.
* Compare with other models: Decision Tree, Random Forest, Logistic Regression.
* Hyperparameter tuning for better performance.

---

## 👨‍💻 Author

* **Brajesh **




Last updated: 2026-10-28 21:26 UTC
