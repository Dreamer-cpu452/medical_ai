
import joblib
import pandas as pd


class DiabetesPrediction:

    def __init__(self):

        self.model = joblib.load(
            "models/diabetes_model.pkl"
        )

    def predict(
        self,
        age,
        bmi,
        glucose
    ):

        data = pd.DataFrame(
            [[
                age,
                bmi,
                glucose
            ]],
            columns=[
                "age",
                "bmi",
                "glucose"
            ]
        )

        prediction = self.model.predict(
            data
        )[0]

        if prediction == 1:

            return {
                "Disease": "Diabetes",
                "Risk": "High"
            }

        return {
            "Disease": "Diabetes",
            "Risk": "Low"
        }

