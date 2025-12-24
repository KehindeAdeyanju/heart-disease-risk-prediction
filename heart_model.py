

"""
Heart Disease Risk Prediction

This script loads clinical data, performs preprocessing and feature engineering,
trains a logistic regression model, evaluates its performance, and visualizes
clinically interpretable results.
"""

# ============================
# 1. Imports
# ============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler


# ============================
# 2. Load Dataset
# ============================
df = pd.read_csv("data/heart.csv")

print("Dataset preview:")
print(df.head())


# ============================
# 3. Basic Inspection
# ============================
print("\nDataset info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())


# ============================
# 4. Feature Engineering
# Create Age Groups
# ============================
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 39, 59, 120],
    labels=["Young", "Middle-age", "Older"]
)

print("\nAge group distribution:")
print(df["age_group"].value_counts())


# ============================
# 5. Feature Selection
# ============================
X = df.drop(columns=["target"])
y = df["target"]


# ============================
# 6. Encode Categorical Features
# ============================
X_encoded = pd.get_dummies(
    X,
    columns=["age_group"],
    drop_first=True
)

print("\nEncoded feature preview:")
print(X_encoded.head())


# ============================
# 7. Train / Test Split
# ============================
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining set size:", X_train.shape)
print("Test set size:", X_test.shape)


# ============================
# 8. Feature Scaling
# ============================
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ============================
# 9. Train Logistic Regression Model
# ============================
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

print("\nModel training completed.")


# ============================
# 10. Make Predictions
# ============================
y_pred = model.predict(X_test_scaled)

print("\nFirst 10 predictions:", y_pred[:10])
print("First 10 actual values:", y_test[:10].values)


# ============================
# 11. Model Evaluation
# ============================
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ============================
# 12. Confusion Matrix (Visual)
# ============================
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()


# ============================
# 13. Model Interpretation
# Feature Importance
# ============================
coefficients = pd.Series(
    model.coef_[0],
    index=X_encoded.columns
).sort_values()

plt.figure(figsize=(8, 6))
coefficients.plot(kind="barh")
plt.axvline(0, color="black", linestyle="--")
plt.xlabel("Coefficient Value")
plt.title("Feature Impact on Heart Disease Risk")
plt.tight_layout()
plt.show()


# ============================
# Script Entry Point
# ============================
if __name__ == "main":
    print("\nHeart Disease Risk Prediction script executed successfully.")

