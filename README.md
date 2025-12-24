# Heart Disease Risk Prediction

This project builds a simple machine learning model to predict the risk of heart disease 
using patient clinical data. It demonstrates data preprocessing, logistic regression, 
model evaluation, and basic medical data interpretation.

---

## Project Structure

heart-disease-risk-prediction/
├── data/
│   └── heart.csv
├── src/
│   └── heart_model.py
├── README.md
├── requirements.txt
└── .gitignore

---

## Dataset

The dataset contains patient clinical features such as age, sex, blood pressure, 
cholesterol levels, and other health indicators.  
The target variable represents the presence or absence of heart disease.

---

## Methodology

1. Loaded and explored the dataset using pandas  
2. Created age groups to improve interpretability  
3. Encoded categorical variables using one-hot encoding  
4. Split the data into training and testing sets  
5. Trained a logistic regression model  
6. Evaluated model performance using accuracy and confusion matrix  
7. Visualized feature importance  

---

## Technologies Used

- Python  
- pandas  
- NumPy  
- scikit-learn  
- matplotlib  
- seaborn  

---

## How to Run

1. Clone the repository  
2. Install dependencies:
3. Run the model:
---

## Future Improvements

- Add feature scaling  
- Try alternative models (Random Forest, XGBoost)  
- Improve evaluation with ROC-AUC  
- Deploy as a simple web application  

---

## Author

Medical professional transitioning into clinical AI and digital health, 
with a focus on safe, interpretable machine learning in healthcare.