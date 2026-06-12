class SpecialistRecommendation:

    def recommend(
        self,
        disease
    ):

        mapping = {

            "Diabetes":
            "Endocrinologist",

            "Heart Disease":
            "Cardiologist",

            "Kidney Disease":
            "Nephrologist",

            "Cancer":
            "Oncologist"
        }

        return mapping.get(
            disease,
            "General Physician"
        )