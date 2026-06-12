class HealthcareChatbot:

    def reply(
        self,
        message
    ):

        message = message.lower()

        if "appointment" in message:

            return "You can book an appointment from Appointment Module."

        elif "doctor" in message:

            return "Doctors are available in Doctor Dashboard."

        elif "diabetes" in message:

            return "Please use Disease Prediction Module."

        return "How may I help you?"