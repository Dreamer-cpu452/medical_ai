class DiagnosticTestRecommendation:

    def recommend_tests(
        self,
        disease
    ):

        tests = {

            "Diabetes":
            ["HbA1c", "Blood Sugar"],

            "Heart Disease":
            ["ECG", "ECHO"],

            "Kidney Disease":
            ["Creatinine", "Urea"],

            "Cancer":
            ["Biopsy", "MRI"]
        }

        return tests.get(
            disease,
            []
        )