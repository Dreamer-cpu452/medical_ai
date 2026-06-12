import sqlite3


class DoctorRegistration:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def add_doctor(
        self,
        doctor_name,
        specialization,
        department,
        experience
    ):

        try:

            conn = sqlite3.connect(
                self.db_path
            )

            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO doctors
                (
                    doctor_name,
                    specialization,
                    department,
                    experience
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
                    doctor_name,
                    specialization,
                    department,
                    experience
                )
            )

            conn.commit()

            conn.close()

            return True

        except Exception as e:

            print(e)

            return False