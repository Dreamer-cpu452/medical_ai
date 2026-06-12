import sqlite3


class PatientRegistration:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def add_patient(
        self,
        full_name,
        age,
        gender,
        blood_group,
        phone
    ):

        try:

            conn = sqlite3.connect(
                self.db_path
            )

            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO patients
                (
                    full_name,
                    age,
                    gender,
                    blood_group,
                    phone
                )
                VALUES
                (
                    ?,
                    ?,
                    ?,
                    ?,
                    ?
                )
                """,
                (
                    full_name,
                    age,
                    gender,
                    blood_group,
                    phone
                )
            )

            conn.commit()

            conn.close()

            return True

        except Exception as e:

            print(e)

            return False