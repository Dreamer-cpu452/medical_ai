class ECGAnalysis:

    def analyze(
        self,
        heart_rate
    ):

        if heart_rate < 60:

            return "Bradycardia"

        elif heart_rate > 100:

            return "Tachycardia"

        return "Normal"