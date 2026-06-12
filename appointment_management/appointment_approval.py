import sqlite3


class AppointmentApproval:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def approve_appointment(
        self,
        appointment_id
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE appointments
            SET status=?
            WHERE appointment_id=?
            """,
            (
                "Approved",
                appointment_id
            )
        )

        conn.commit()

        conn.close()

        return True