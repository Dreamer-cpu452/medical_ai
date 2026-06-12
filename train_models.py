
import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

os.makedirs("models", exist_ok=True)

# -------------------------
# Diabetes Model
# -------------------------

df = pd.read_csv("datasets/diabetes.csv")

X = df[["age", "bmi", "glucose"]]
y = df["outcome"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(
    model,
    "models/diabetes_model.pkl"
)

# -------------------------
# Heart Model
# -------------------------

df = pd.read_csv("datasets/heart_disease.csv")

X = df[
    [
        "age",
        "cholesterol",
        "blood_pressure"
    ]
]

y = df["outcome"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(
    model,
    "models/heart_model.pkl"
)

# -------------------------
# Kidney Model
# -------------------------

df = pd.read_csv("datasets/kidney_disease.csv")

X = df[
    [
        "age",
        "creatinine",
        "blood_urea"
    ]
]

y = df["outcome"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(
    model,
    "models/kidney_model.pkl"
)

# -------------------------
# Cancer Model
# -------------------------

df = pd.read_csv("datasets/cancer_risk.csv")

X = df[
    [
        "age",
        "tumor_size",
        "smoking_years"
    ]
]

y = df["outcome"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(
    model,
    "models/cancer_model.pkl"
)

print(
    "Models trained and saved successfully."
)

