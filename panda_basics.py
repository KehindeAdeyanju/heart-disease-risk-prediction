


  #import pandas as pd
 #data ={
   # "Name": ["Kehinde", "Adeyanju", "Ebenezer", "Sarah"],
#"Age":  [28, 29, 30, 35],
   # "Sex": ["M", "M", "M", "F"],
  #  "Diagnosis": ["Hypertension", "Diabetes", "Hypertension", "Diabetes"]

#}
 #df = pd.DataFrame(data)

#(df.groupby(["Sex", "Diagnosis"]) ["Age"].count())

#import pandas as pd
#import matplotlib.pyplot as plt

#df = pd.read_csv("heart.csv")
#df["age_group"] = pd.cut(
#    df["age"],
#    bins = [0, 39, 59, 120],
#    labels = ["Young", "Middle-age", "Older"]
#)



#df.groupby("age_group")["target"].mean().plot(kind="bar")
#plt.title ("Heart Disease Proportion by Age Group")
#plt.xlabel("Age Group")
#plt.ylabel("Proportion with Heart Disease")

#plt.show()

#print (df.groupby("sex")["target"].mean())

#print (df["age"].describe())



#print(df[["age", "age_group"]].head)

#print (df.groupby("age_group")["target"].mean())

#(df.groupby(["age_group", "sex"], observed=True)["target"]
      #.mean()
     # .unstack()
      #.plot(kind= "bar")
 #)
#plt.title("Heart Disease Proportion by Age Group and Sex")
#plt.xlabel("Age Group")
#plt.ylabel("Proportion with Heart Disease")
#plt.legend(title="Sex (0 = Female, 1 = Male)")
#plt.show()

#print(df.groupby(["age_group", "sex"])["target"].mean())

#print (df.head())
#y = df["target"]
#print (y.head())
#x = df.drop("target", axis =1)
#print(x.head())


########

#print (x.dtypes)

#x["age_group"].head()
#x_encoded = pd.get_dummies(x, columns=["age_group"], drop_first=True)
#print (x_encoded.head())

#import pandas as pd

from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression(max_iter=1000)
# from sklearn.metrics import confusion_matrix
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df = pd.read_csv("heart.csv")
# df["age_group"] = pd.cut(
#    df["age"],
#   bins = [0, 39, 59, 120],
#     labels = ["Young", "Middle-age", "Older"]
# )
# x = df.drop(columns=["target"])
# y = df["target"]
# x_encoded = pd.get_dummies(
#x,
 #   columns=["age_group"],
 #   drop_first=True
#)
#x = x_encoded
#x_train, x_test, y_train, y_test = train_test_split(
#    x,
#    y,
#    test_size=0.2,
#   random_state=42
#)
#model.fit(x_train, y_train)


 ####



# Generate predictions
#y_pred = model.predict(x_test)

# Confusion matrix
#cm = confusion_matrix(y_test, y_pred)

# Plot
#plt.figure(figsize=(6, 4))
#sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
#            xticklabels=["No Disease", "Disease"],
#            yticklabels=["No Disease", "Disease"])

# plt.xlabel("Predicted")
# plt.ylabel("Actual")
# plt.title("Confusion Matrix – Heart Disease Model")
# plt.show()
#
# ===============================
# Heart Disease Risk Prediction
# ===============================

# 1. Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2. Load data
df = pd.read_csv("heart.csv")

# 3. Create age groups (clinical reasoning)
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 39, 59, 120],
    labels=["Young", "Middle-age", "Older"]
)

# 4. Separate features and target
X = df.drop(columns=["target"])
y = df["target"]

# 5. Encode categorical variables
X_encoded = pd.get_dummies(X, columns=["age_group"], drop_first=True)

# 6. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

# 7. Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 8. Predictions
y_pred = model.predict(X_test)

# 9. Model evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 10. Confusion matrix visualization
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# 11. Feature importance (coefficients)
coefficients = pd.Series(
    model.coef_[0],
    index=X_encoded.columns
).sort_values()

plt.figure(figsize=(8, 6))
coefficients.plot(kind="barh")
plt.title("Feature Impact on Heart Disease Risk")
plt.xlabel("Coefficient Value")
plt.tight_layout()
plt.show()