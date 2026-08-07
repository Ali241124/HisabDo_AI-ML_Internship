# Install Libraries

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field
import joblib
import numpy as np

# Load Model And Scaler

model = joblib.load("student_model.pkl")
scaler= joblib.load("scaler.pkl")

app = FastAPI(title = "Student Performance Prediction API")

# Request Schema

class StudentData(BaseModel):
    attendance: float = Field(..., ge= 0, le= 100)
    assignment_score: float = Field(..., ge= 0, le= 100)
    midterm_score: float = Field(..., ge= 0, le= 100)
    final_score: float = Field(..., ge= 0, le= 100)

@app.get("/")
def home():
    return {"message": "Student Performance Prediction API is running!"}

@app.post("/predict")
def predict(data: StudentData):

    try:
        # Feature Engineering
        average_score = (data.assignment_score + data.midterm_score) / 2
        features = np.array([[
            data.attendance,
            data.assignment_score,
            data.midterm_score,
            average_score
        ]]
        )

        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0]

        result = "Pass" if prediction == 1 else "Fail"
        confidence = float(max(probability))

        return {
            "prediction": result,
            "confidence": round(confidence, 4)
        }
    except Exception as e:
        raise HTTPException(status_code= 500, detail=str(e))
    
