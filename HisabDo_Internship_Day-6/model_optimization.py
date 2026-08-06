# Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    RocCurveDisplay
)

# Load Dataset

df = pd.read_excel("student_performance_dataset.xlsx")

# Data Cleaning

df["Assignment Score"] = df["Assignment Score"].fillna(df["Assignment Score"].mean())

df.loc[df["Attendance"] > 100, "Attendance"] = 100
df.loc[df["Attendance"] < 0, "Attendance"] = 0

# Feature Engineering

df["Average Score"] = (df["Assignment Score"] + df["Midterm Score"] + df["Final Score"]) / 3

# Target

df["Pass"] = (df["Final Score"] >= 60).astype(int)

# Features

X = df[
    [
        "Attendance",
        "Assignment Score",
        "Midterm Score",
        "Average Score"
    ]
]

y = df["Pass"]

# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size= 0.20,
    random_state=42
)

# Feature Scaling

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Base Model

base_model = LogisticRegression(max_iter= 1000)
base_model.fit(X_train_scaled, y_train)
base_pred = base_model.predict(X_test_scaled)

# Hyperparameter Tuning

parameters = {
    "C":[0.01,0.1,1,10,100],
    "solver":["liblinear", "lbfgs"]
}

grid = GridSearchCV(
    LogisticRegression(max_iter=1000),
    parameters,
    cv = 5,
    scoring="accuracy"
)

grid.fit(X_train_scaled, y_train)
best_model = grid.best_estimator_
best_pred = best_model.predict(X_test_scaled)

# Evaluation Function

def evaluate(name, y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    roc = roc_auc_score(y_true, y_pred)
    print("-"*60)
    print(name)
    print("-"*60)

    print("Accuracy:", round(accuracy,2))
    print("Precision:", round(precision,2))
    print("Recall:", round(recall,2))
    print("F1 Score:", round(f1,2))
    print("ROC-AUC:", round(roc,2))

    return accuracy, precision, recall, f1, roc

# Evaluate

base_metrics = evaluate(
    "Base Logistic Regression",
    y_test,
    base_pred
)

best_metrics = evaluate(
    "Tuned Logistic Regression",
    y_test,
    best_pred
)

print("\nBest Parameters:")
print(grid.best_params_)

# Comparison Table

comparison = pd.DataFrame({

    "Model":[
        "Base Model",
        "Best Model"
    ],
    "Accuracy":[
        base_metrics[0],
        best_metrics[0]
    ],
    "Precision":[
        base_metrics[1],
        best_metrics[1]
    ],
    "Recall":[
        base_metrics[2],
        best_metrics[2]
    ],
    "F1 Score":[
        base_metrics[3],
        best_metrics[3]
    ],
    "ROC-AUC":[
        base_metrics[4],
        best_metrics[4]
    ]
    }
    )

print("\nComparison Table")
print(comparison)

# Accuracy Comparison Chart

plt.figure(figsize=(6,4))
plt.bar(
    comparison["Model"],
    comparison["Accuracy"]
)
plt.title("Accuracy Comparison")
plt.ylabel("Accuracy")
plt.tight_layout()
plt.savefig("charts/accuracy_comparison.png")
plt.show()

# Confusion Matrix

ConfusionMatrixDisplay.from_predictions(
    y_test,
    best_pred
)
plt.title("Confusion Matrix")
plt.savefig("charts/confusion_matrix.png")
plt.show()

# ROC Curve

RocCurveDisplay.from_estimator(
    best_model,
    X_test_scaled,
    y_test
)
plt.title("ROC Curve")
plt.savefig("charts/roc_curve.png")
plt.show()