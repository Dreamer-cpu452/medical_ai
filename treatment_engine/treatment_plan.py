class TreatmentPlan:

    def generate_plan(
        self,
        disease
    ):

        plans = {

            "Diabetes": [
                "Low Sugar Diet",
                "Daily Exercise",
                "Regular Blood Sugar Monitoring"
            ],

            "Heart Disease": [
                "Low Fat Diet",
                "Cardiology Consultation",
                "Blood Pressure Monitoring"
            ],

            "Kidney Disease": [
                "Low Sodium Diet",
                "Hydration Monitoring",
                "Kidney Function Tests"
            ],

            "Cancer": [
                "Oncology Consultation",
                "Chemotherapy Evaluation",
                "Regular Scans"
            ]
        }

        return plans.get(
            disease,
            ["General Physician Consultation"]
        )