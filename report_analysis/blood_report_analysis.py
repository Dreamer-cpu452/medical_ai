class BloodReportAnalysis:

    def analyze(
        self,
        hemoglobin,
        sugar
    ):

        result = {}

        if hemoglobin < 12:

            result["Hemoglobin"] = "Low"

        else:

            result["Hemoglobin"] = "Normal"

        if sugar > 140:

            result["Sugar"] = "High"

        else:

            result["Sugar"] = "Normal"

        return result