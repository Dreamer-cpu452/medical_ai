import sqlite3

from authentication.password_utils import PasswordUtils


class UserLogin:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def login(
        self,
        email,
        password
    ):

        try:

            conn = sqlite3.connect(
                self.db_path
            )

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT *
                FROM users
                WHERE email=?
                """,
                (email,)
            )

            user = cursor.fetchone()

            conn.close()

            if not user:

                return None

            stored_password = user[3]

            if PasswordUtils.verify_password(
                password,
                stored_password
            ):

                return user

            return None

        except Exception as e:

            print(e)

            return None