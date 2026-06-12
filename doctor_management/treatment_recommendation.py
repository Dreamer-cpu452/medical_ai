class TreatmentRecommendation:

    def recommend(
        self,
        disease
    ):

        recommendations = {

            "Diabetes":
            [
                "Low Sugar Diet",
                "Daily Walking",
                "Blood Sugar Monitoring"
            ],

            "Heart Disease":
            [
                "Low Fat Diet",
                "Cardio Exercise",
                "Blood Pressure Monitoring"
            ],

            "Kidney Disease":
            [
                "Low Sodium Diet",
                "Hydration Monitoring",
                "Kidney Function Tests"
            ],

            "Cancer":
            [
                "Oncology Consultation",
                "Chemotherapy Evaluation",
                "Regular Screening"
            ]
        }

        return recommendations.get(
            disease,
            ["Consult Specialist"]
        )