class FAQEngine:

    def answer(
        self,
        question
    ):

        faq = {

            "hospital timings":
            "24 Hours",

            "emergency":
            "Available 24/7",

            "appointment":
            "Online Booking Available"
        }

        return faq.get(
            question.lower(),
            "Information Not Found"
        )