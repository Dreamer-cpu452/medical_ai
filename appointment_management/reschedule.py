import sqlite3


class AppointmentReschedule:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def reschedule(
        self,
        appointment_id,
        new_date
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE appointments
            SET appointment_date=?
            WHERE appointment_id=?
            """,
            (
                new_date,
                appointment_id
            )
        )

        conn.commit()

        conn.close()

        return True