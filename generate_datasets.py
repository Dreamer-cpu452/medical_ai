import pandas as pd
import random
import os

# -----------------------------
# Create Dataset Folder
# -----------------------------

os.makedirs(
    "datasets",
    exist_ok=True
)

# -----------------------------
# Diabetes Dataset
# -----------------------------

diabetes_data = []

for i in range(200):

    age = random.randint(18, 80)

    bmi = round(
        random.uniform(18, 40),
        2
    )

    glucose = random.randint(
        70,
        250
    )

    outcome = random.randint(
        0,
        1
    )

    diabetes_data.append([
        age,
        bmi,
        glucose,
        outcome
    ])

pd.DataFrame(
    diabetes_data,
    columns=[
        "age",
        "bmi",
        "glucose",
        "outcome"
    ]
).to_csv(
    "datasets/diabetes.csv",
    index=False
)

# -----------------------------
# Heart Disease Dataset
# -----------------------------

heart_data = []

for i in range(200):

    age = random.randint(
        20,
        90
    )

    cholesterol = random.randint(
        100,
        350
    )

    blood_pressure = random.randint(
        80,
        200
    )

    outcome = random.randint(
        0,
        1
    )

    heart_data.append([
        age,
        cholesterol,
        blood_pressure,
        outcome
    ])

pd.DataFrame(
    heart_data,
    columns=[
        "age",
        "cholesterol",
        "blood_pressure",
        "outcome"
    ]
).to_csv(
    "datasets/heart_disease.csv",
    index=False
)

# -----------------------------
# Kidney Disease Dataset
# -----------------------------

kidney_data = []

for i in range(200):

    age = random.randint(
        18,
        85
    )

    creatinine = round(
        random.uniform(
            0.5,
            5.0
        ),
        2
    )

    blood_urea = random.randint(
        10,
        120
    )

    outcome = random.randint(
        0,
        1
    )

    kidney_data.append([
        age,
        creatinine,
        blood_urea,
        outcome
    ])

pd.DataFrame(
    kidney_data,
    columns=[
        "age",
        "creatinine",
        "blood_urea",
        "outcome"
    ]
).to_csv(
    "datasets/kidney_disease.csv",
    index=False
)

# -----------------------------
# Cancer Risk Dataset
# -----------------------------

cancer_data = []

for i in range(200):

    age = random.randint(
        20,
        90
    )

    tumor_size = random.randint(
        1,
        50
    )

    smoking_years = random.randint(
        0,
        40
    )

    outcome = random.randint(
        0,
        1
    )

    cancer_data.append([
        age,
        tumor_size,
        smoking_years,
        outcome
    ])

pd.DataFrame(
    cancer_data,
    columns=[
        "age",
        "tumor_size",
        "smoking_years",
        "outcome"
    ]
).to_csv(
    "datasets/cancer_risk.csv",
    index=False
)

# -----------------------------
# Patient History Dataset
# -----------------------------

diseases = [
    "Diabetes",
    "Heart Disease",
    "Kidney Disease",
    "Cancer"
]

patient_history = []

for i in range(
    1,
    201
):

    patient_history.append([

        i,

        f"Patient_{i}",

        random.choice(
            diseases
        )
    ])

pd.DataFrame(
    patient_history,
    columns=[
        "patient_id",
        "name",
        "disease"
    ]
).to_csv(
    "datasets/patient_history.csv",
    index=False
)

print(
    "All datasets generated successfully."
)