import sqlite3


class AllergyManager:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def add_allergy(
        self,
        patient_id,
        allergy
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS allergies(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                allergy TEXT
            )
            """
        )

        cursor.execute(
            """
            INSERT INTO allergies(
                patient_id,
                allergy
            )
            VALUES(
                ?,
                ?
            )
            """,
            (
                patient_id,
                allergy
            )
        )

        conn.commit()

        conn.close()

        return True