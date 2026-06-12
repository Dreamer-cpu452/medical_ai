from ai_prediction.diabetes_prediction import DiabetesPrediction
from ai_prediction.heart_prediction import HeartPrediction
from ai_prediction.kidney_prediction import KidneyPrediction
from ai_prediction.cancer_prediction import CancerPrediction


class DiseasePrediction:

    def __init__(self):

        self.diabetes = DiabetesPrediction()

        self.heart = HeartPrediction()

        self.kidney = KidneyPrediction()

        self.cancer = CancerPrediction()

    def predict_diabetes(
        self,
        age,
        bmi,
        glucose
    ):

        return self.diabetes.predict(
            age,
            bmi,
            glucose
        )

    def predict_heart(
        self,
        age,
        cholesterol,
        blood_pressure
    ):

        return self.heart.predict(
            age,
            cholesterol,
            blood_pressure
        )

    def predict_kidney(
        self,
        age,
        creatinine,
        blood_urea
    ):

        return self.kidney.predict(
            age,
            creatinine,
            blood_urea
        )

    def predict_cancer(
        self,
        age,
        tumor_size,
        smoking_years
    ):

        return self.cancer.predict(
            age,
            tumor_size,
            smoking_years
        )