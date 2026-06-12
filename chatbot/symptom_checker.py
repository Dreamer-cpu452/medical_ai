class SymptomChecker:

    def check(
        self,
        symptom
    ):

        symptom = symptom.lower()

        if "fever" in symptom:

            return "Possible Infection"

        elif "chest pain" in symptom:

            return "Possible Heart Condition"

        elif "cough" in symptom:

            return "Respiratory Issue"

        return "Consult Doctor"