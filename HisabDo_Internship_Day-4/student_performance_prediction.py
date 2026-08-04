# Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

# Load Dataset

df = pd.read_excel("student_performance_dataset.xlsx")

# Data Cleaning

df["Assignment Score"] = df["Assignment Score"].fillna(
    df["Assignment Score"].mean()
)

df.loc[df["Attendance"] > 100 , "Attendance"] = 100
df.loc[df["Attendance"] < 0 , "Attendance"] = 0 

# Create Target Columns

df["Pass"] = (df["Final Score"] >= 60).astype(int)

# Features and Target

X = df[[
    "Attendance",
    "Assignment Score",
    "Midterm Score"
]]

y = df["Pass"]

# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Logistic Regression

model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction

y_pred = model.predict(X_test)

# Evaluation

accuracy = accuracy_score(y_test, y_pred)

print("-"*60)
print("MODEL ACCURACY")
print("-"*60)
print(f"Accuracy: {accuracy:.2f}")

print("\nConfusion Matrix")
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\nClassification Report")
cr= classification_report(y_test, y_pred)
print(cr)

print("-"*60)
print("Visualization")
print("-"*60)

# Pass/Fail Distribution

plt.figure(figsize=(6,4))
df["Pass"].value_counts().plot(kind="bar")
plt.title("Pass/Fail Distribution")
plt.xlabel("Pass(1) / Fail (0)")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("charts/pass_fail_distribution.png")
plt.show()

# Confusion Matrix

disp = ConfusionMatrixDisplay(
    confusion_matrix= cm,
    display_labels=["Fail", "Pass"]
)
disp.plot()
plt.title("Confusion Matrix")
plt.savefig("charts/confusion_matrix.png")
plt.show()
