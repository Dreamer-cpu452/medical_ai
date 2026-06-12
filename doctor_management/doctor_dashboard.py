import sqlite3


class DoctorDashboard:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def get_doctors(self):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM doctors
            """
        )

        doctors = cursor.fetchall()

        conn.close()

        return doctors