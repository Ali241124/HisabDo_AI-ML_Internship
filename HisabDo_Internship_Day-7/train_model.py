# Install Libraries

import pandas as pd
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load Dataset

df = pd.read_excel("student_performance_dataset.xlsx")

# Data Cleaning

df["Assignment Score"] = df["Assignment Score"].fillna(df["Assignment Score"].mean())
df.loc[df["Attendance"] > 100, "Attendance"] = 100
df.loc[df["Attendance"] < 0, "Attendance"] = 0

# Feature Engineering

df["Average Score"] = df["Assignment Score"] + df["Midterm Score"] / 2

# Target

df["Pass"] = (df["Final Score"] >= 60).astype(int)

# Features

X = df[[
    "Attendance",
    "Assignment Score",
    "Midterm Score",
    "Average Score"
]]

y = df["Pass"]

# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size= 0.2,
    random_state= 42
)

# Scaling

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train Model

model = LogisticRegression(C= 0.1, solver="liblinear", max_iter= 1000)
model.fit(X_train_scaled, y_train)

# Save model and Scaler

joblib.dump(model, "student_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model and Scaler saved successfully.")