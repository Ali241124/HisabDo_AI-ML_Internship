# Day 7 - Student Performance Prediction API

## Objective

Deploy the trained Logistic Regression model as a REST API using FastAPI.

## Installation

```bash
pip install -r requirements.txt
```

## Train the Model

```bash
python train_model.py
```

This creates:

* `student_model.pkl`
* `scaler.pkl`

## Run the API

```bash
uvicorn app:app --reload
```

API URL: `http://127.0.0.1:8000`

Swagger Docs: `http://127.0.0.1:8000/docs`

## Endpoint

**POST /predict**

### Request

```json
{
  "attendance": 88,
  "assignment_score": 82,
  "midterm_score": 79,
  "final_score": 84
}
```

### Response

```json
{
  "prediction": "Pass",
  "confidence": 0.9567
}
```

## Features

* Input validation
* JSON response
* Confidence score
* Error handling
* FastAPI automatic documentation
