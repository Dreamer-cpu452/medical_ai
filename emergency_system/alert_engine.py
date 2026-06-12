class AlertEngine:

    def generate_alert(
        self,
        oxygen_level
    ):

        if oxygen_level < 85:

            return "CRITICAL ALERT"

        elif oxygen_level < 92:

            return "WARNING ALERT"

        return "NORMAL"