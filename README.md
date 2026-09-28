# 💳 Credit Scoring & Risk Intelligence System

A lightweight, high-performance machine learning pipeline and interactive desktop GUI built entirely in **Pure Python** with zero external dependencies. Designed specifically to evaluate credit risk, compute core classification metrics, and deliver real-time risk intelligence through a modern dashboard.

---

## 🚀 Key Features

* **Pure Python Architecture:** Engineered without heavy external libraries (such as `pandas` or `scikit-learn`), making it resilient against environment setup or `pip` installation errors.
* **Synthetic Data Generation:** Simulates realistic applicant profiles featuring annual income, total debt, payment history scores, credit age, and credit utilization.
* **Advanced Feature Engineering:** Computes financial risk factors, including Debt-to-Income (DTI) ratios and multi-variable risk scoring functions.
* **Rigorous Model Evaluation:** Evaluates performance across an 80/20 train-test split, calculating **Accuracy, Precision, Recall, and F1-Harmonic Score**.
* **Confusion Matrix Breakdown:** Tracks True Negatives, False Positives (Type I Error), False Negatives (Type II Error), and True Positives.
* **Modern Desktop GUI Dashboard:** Features a clean, custom dark slate UI built using `tkinter` with structured metric cards and visual highlights.

---

## 📊 Performance Metrics

* **Dataset Size:** 5,000 Applicants
* **Accuracy:** 0.7030
* **Precision:** 0.7039
* **Recall:** 0.9019
* **F1-Score:** 0.7907

---

## 🛠️ Getting Started & Installation

Because this application relies exclusively on Python's standard library, no complex package installations are required!

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt in the project directory.
3. Run the application using Python:
   ```bash
   py credit_model.py

