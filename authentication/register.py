import sqlite3

from authentication.password_utils import PasswordUtils


class UserRegister:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def register_user(
        self,
        full_name,
        email,
        password,
        role
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

            existing_user = cursor.fetchone()

            if existing_user:

                conn.close()

                return False

            hashed_password = (
                PasswordUtils.hash_password(
                    password
                )
            )

            cursor.execute(
                """
                INSERT INTO users
                (
                    full_name,
                    email,
                    password,
                    role
                )
                VALUES
                (
                    ?,
                    ?,
                    ?,
                    ?
                )
                """,
                (
                    full_name,
                    email,
                    hashed_password,
                    role
                )
            )

            conn.commit()

            conn.close()

            return True

        except Exception as e:

            print(e)

            return False