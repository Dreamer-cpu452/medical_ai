class RecoveryPrediction:

    def predict(
        self,
        age,
        severity
    ):

        score = 100 - (
            age * 0.3 +
            severity * 10
        )

        return max(
            0,
            round(score, 2)
        )