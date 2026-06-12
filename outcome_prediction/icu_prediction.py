class ICUPrediction:

    def predict(
        self,
        oxygen_level
    ):

        if oxygen_level < 85:

            return "High"

        elif oxygen_level < 92:

            return "Medium"

        return "Low"