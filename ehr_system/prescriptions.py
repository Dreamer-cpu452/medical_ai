import sqlite3


class PrescriptionManager:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def add_prescription(
        self,
        patient_id,
        doctor_id,
        medicine,
        dosage
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS prescriptions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                doctor_id INTEGER,
                medicine TEXT,
                dosage TEXT
            )
            """
        )

        cursor.execute(
            """
            INSERT INTO prescriptions(
                patient_id,
                doctor_id,
                medicine,
                dosage
            )
            VALUES(
                ?,
                ?,
                ?,
                ?
            )
            """,
            (
                patient_id,
                doctor_id,
                medicine,
                dosage
            )
        )

        conn.commit()

        conn.close()

        return True