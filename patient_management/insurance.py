import sqlite3


class InsuranceManager:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def add_insurance(
        self,
        patient_id,
        company,
        policy_number
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS insurance(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                company TEXT,
                policy_number TEXT
            )
            """
        )

        cursor.execute(
            """
            INSERT INTO insurance(
                patient_id,
                company,
                policy_number
            )
            VALUES(
                ?,
                ?,
                ?
            )
            """,
            (
                patient_id,
                company,
                policy_number
            )
        )

        conn.commit()

        conn.close()

        return True