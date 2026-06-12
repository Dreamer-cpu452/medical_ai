
class Validators:

    @staticmethod
    def validate_email(email):

        return "@" in email

    @staticmethod
    def validate_phone(phone):

        return phone.isdigit() and len(phone) == 10
