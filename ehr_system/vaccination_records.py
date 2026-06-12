import sqlite3


class VaccinationRecords:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def add_vaccination(
        self,
        patient_id,
        vaccine_name,
        vaccination_date
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS vaccinations(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                vaccine_name TEXT,
                vaccination_date TEXT
            )
            """
        )

        cursor.execute(
            """
            INSERT INTO vaccinations(
                patient_id,
                vaccine_name,
                vaccination_date
            )
            VALUES(
                ?,
                ?,
                ?
            )
            """,
            (
                patient_id,
                vaccine_name,
                vaccination_date
            )
        )

        conn.commit()

        conn.close()

        return True