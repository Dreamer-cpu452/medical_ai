import bcrypt


class PasswordUtils:

    @staticmethod
    def hash_password(password):

        return bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()

    @staticmethod
    def verify_password(
        password,
        hashed_password
    ):

        return bcrypt.checkpw(
            password.encode(),
            hashed_password.encode()
        )