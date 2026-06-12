import sqlite3


class TreatmentHistory:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def add_treatment(
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
            CREATE TABLE IF NOT EXISTS treatment_history(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                diagnosis TEXT,
                treatment TEXT
            )
            """
        )

        cursor.execute(
            """
            INSERT INTO treatment_history(
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