class MortalityPrediction:

    def predict(
        self,
        age,
        severity
    ):

        risk = (
            age * 0.4 +
            severity * 8
        )

        if risk > 70:

            return "High"

        elif risk > 40:

            return "Medium"

        return "Low"