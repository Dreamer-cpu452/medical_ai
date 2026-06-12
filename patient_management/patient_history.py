import sqlite3


class PatientHistory:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def get_all_patients(self):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM patients
            """
        )

        data = cursor.fetchall()

        conn.close()

        return data