class MedicationGuidance:

    def get_guidance(
        self,
        disease
    ):

        guidance = {

            "Diabetes":
            "Take medicines regularly and monitor sugar.",

            "Heart Disease":
            "Avoid oily food and monitor BP.",

            "Kidney Disease":
            "Maintain hydration and avoid excess salt.",

            "Cancer":
            "Follow oncologist treatment schedule."
        }

        return guidance.get(
            disease,
            "Consult Doctor"
        )