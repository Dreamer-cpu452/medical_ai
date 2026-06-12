import joblib
import pandas as pd


class CancerPrediction:

    def __init__(self):

        self.model = joblib.load(
            "models/cancer_model.pkl"
        )

    def predict(
        self,
        age,
        tumor_size,
        smoking_years
    ):

        data = pd.DataFrame(
            [[
                age,
                tumor_size,
                smoking_years
            ]],
            columns=[
                "age",
                "tumor_size",
                "smoking_years"
            ]
        )

        prediction = self.model.predict(
            data
        )[0]

        if prediction == 1:

            return {

                "Disease":
                "Cancer Risk",

                "Risk":
                "High"
            }

        return {

            "Disease":
            "Cancer Risk",

            "Risk":
            "Low"
        }