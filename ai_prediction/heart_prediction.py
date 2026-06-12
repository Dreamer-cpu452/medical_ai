import joblib
import pandas as pd


class HeartPrediction:

    def __init__(self):

        self.model = joblib.load(
            "models/heart_model.pkl"
        )

    def predict(
        self,
        age,
        cholesterol,
        blood_pressure
    ):

        data = pd.DataFrame(
            [[
                age,
                cholesterol,
                blood_pressure
            ]],
            columns=[
                "age",
                "cholesterol",
                "blood_pressure"
            ]
        )

        prediction = self.model.predict(
            data
        )[0]

        if prediction == 1:

            return {

                "Disease":
                "Heart Disease",

                "Risk":
                "High"
            }

        return {

            "Disease":
            "Heart Disease",

            "Risk":
            "Low"
        }