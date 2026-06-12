import sqlite3


class MedicalRecords:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def add_record(
        self,
        patient_id,
        diagnosis,
        treatment
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS medical_records(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                diagnosis TEXT,
                treatment TEXT
            )
            """
        )

        cursor.execute(
            """
            INSERT INTO medical_records(
                patient_id,
                diagnosis,
                treatment
            )
            VALUES(
                ?,
                ?,
                ?
            )
            """,
            (
                patient_id,
                diagnosis,
                treatment
            )
        )

        conn.commit()

        conn.close()

        return True