# Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
#   Load Dataset

df = pd.read_excel("student_performance_dataset.xlsx")

# Clean Dataset

df["Assignment Score"] = df["Assignment Score"].fillna(df["Assignment Score"].mean())

df.loc[df["Attendance"] > 100, "Attendance"] = 100
df.loc[df["Attendance"] < 0, "Attendance"] = 0

# Target Variables

df["Pass"] = (df["Final Score"] >= 60).astype(int)

# Features

X = df[
    [
    "Attendance",
    "Assignment Score",
    "Midterm Score"
]
]

y = df["Pass"]

# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Logistic Regression

log_model = LogisticRegression()
log_model.fit(X_train, y_train)
log_pred = log_model.predict(X_test)

# Decision Tree

tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)
tree_pred = tree_model.predict(X_test)

# Evaluation Function

def evaluate_model(name,y_true,y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    print("-"*60)
    print(name)
    print("-"*60)

    print("Accuracy :", round(accuracy,2))
    print("Precision :", round(precision,2))
    print("Recall :", round(recall,2))
    print("F1 Score :", round(f1,2))

    print("\nClassification Report")
    print(classification_report(y_true, y_pred))

    return accuracy, precision, recall, f1

# Evaluate Both Models

log_metrics = evaluate_model(
    "Logistic Regression",
    y_test,
    log_pred
)
tree_metrics = evaluate_model(
    "Decision Tree",
    y_test,
    tree_pred
)

# Comparison Table 

comparison = pd.DataFrame(
    {
        "Model":[
            "Logistic Regression",
            "Decision Tree"
        ],
        "Accuracy":[
            log_metrics[0],
            tree_metrics[0]
        ],
        "Precision":[
                    log_metrics[1],
                    tree_metrics[1]
                ],
        "Recall":[
                    log_metrics[2],
                    tree_metrics[2]
                ],
        "F1 Score":[
                    log_metrics[3],
                    tree_metrics[3]
                ],
    }
)

print("\n")
print("-"*60)
print("MODEL COMPARISON")
print("-"*60)
print(comparison)

# Visualization

# Pass / Fail Distribution

plt.figure(figsize=(6,4))
df["Pass"].value_counts().plot(kind="bar")
plt.title("Pass / Fail Distribution")
plt.xlabel("Pass(1) / Fail(0)")
plt.ylabel("Student")
plt.tight_layout()
plt.savefig("charts/pass_fail_distribution.png")
plt.show()

# Logistic Regression Confusion Matrix

ConfusionMatrixDisplay.from_predictions(
    y_test,
    log_pred
)
plt.title("Logistic Regression")
plt.savefig("charts/logistic_regression_confusion_matrix.png")
plt.show()

# Decision Tree Confusion Matrix

ConfusionMatrixDisplay.from_predictions(
    y_test,
    tree_pred
)
plt.title("Decision Tree")
plt.savefig("charts/decision_tree_confusion_matrix.png")
plt.show()

# Accuracy Comparison

plt.figure(figsize=(6,4))
plt.bar(
    comparison["Model"],
    comparison["Accuracy"]
)
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.tight_layout()
plt.savefig("charts/model_accuracy_comparison.png")
plt.show()