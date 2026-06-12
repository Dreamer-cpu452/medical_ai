import sqlite3


class AppointmentBooking:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def book_appointment(
        self,
        patient_id,
        doctor_id,
        appointment_date
    ):

        try:

            conn = sqlite3.connect(
                self.db_path
            )

            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO appointments
                (
                    patient_id,
                    doctor_id,
                    appointment_date,
                    status
                )
                VALUES
                (
                    ?,
                    ?,
                    ?,
                    ?
                )
                """,
                (
                    patient_id,
                    doctor_id,
                    appointment_date,
                    "Pending"
                )
            )

            conn.commit()

            conn.close()

            return True

        except Exception as e:

            print(e)

            return False