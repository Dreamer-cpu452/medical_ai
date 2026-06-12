import sqlite3


class DoctorSchedule:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def add_schedule(
        self,
        doctor_id,
        available_day,
        available_time
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS doctor_schedule(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                doctor_id INTEGER,
                available_day TEXT,
                available_time TEXT
            )
            """
        )

        cursor.execute(
            """
            INSERT INTO doctor_schedule(
                doctor_id,
                available_day,
                available_time
            )
            VALUES(
                ?,
                ?,
                ?
            )
            """,
            (
                doctor_id,
                available_day,
                available_time
            )
        )

        conn.commit()

        conn.close()

        return True