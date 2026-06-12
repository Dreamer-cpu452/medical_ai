class StaffPrediction:

    def predict_needed(
        self,
        patients
    ):

        return max(
            2,
            patients // 5
        )