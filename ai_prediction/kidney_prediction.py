import joblib
import pandas as pd


class KidneyPrediction:

    def __init__(self):

        self.model = joblib.load(
            "models/kidney_model.pkl"
        )

    def predict(
        self,
        age,
        creatinine,
        blood_urea
    ):

        data = pd.DataFrame(
            [[
                age,
                creatinine,
                blood_urea
            ]],
            columns=[
                "age",
                "creatinine",
                "blood_urea"
            ]
        )

        prediction = self.model.predict(
            data
        )[0]

        if prediction == 1:

            return {

                "Disease":
                "Kidney Disease",

                "Risk":
                "High"
            }

        return {

            "Disease":
            "Kidney Disease",

            "Risk":
            "Low"
        }