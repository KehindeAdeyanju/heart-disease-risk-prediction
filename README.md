# Heart Disease Risk Prediction

This project uses machine learning to predict the risk of heart disease based on patient health data.

The goal is to demonstrate a complete data science workflow including data preprocessing, feature engineering, model training, evaluation, and visualisation.

---

## 📊 Dataset
The dataset contains clinical features such as:
- Age
- Sex
- Blood pressure
- Cholesterol
- Chest pain type
- Heart disease outcome (target)

---

## 🛠️ Technologies Used
- Python
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn

---

## ⚙️ Workflow
1. Load and inspect the dataset
2. Engineer age groups for better interpretability
3. Encode categorical features
4. Split data into training and test sets
5. Scale features
6. Train a Logistic Regression model
7. Evaluate model performance
8. Visualise results and feature importance

---

## 📈 Model Performance
- Accuracy: ~80% (varies slightly per run)
- Evaluation metrics include confusion matrix and classification report

---

## 📊 Visualisations
- Confusion matrix heatmap
- Feature importance plot showing factors influencing heart disease risk

---

## 🚀 How to Run
`bash
pip install -r requirements.txt
python heart_model.py
