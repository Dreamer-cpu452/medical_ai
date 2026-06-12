import sqlite3


class DiagnosticReports:

    def __init__(self):

        self.db_path = "database/healthcare.db"

    def add_report(
        self,
        patient_id,
        report_name,
        findings
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS diagnostic_reports(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                report_name TEXT,
                findings TEXT
            )
            """
        )

        cursor.execute(
            """
            INSERT INTO diagnostic_reports(
                patient_id,
                report_name,
                findings
            )
            VALUES(
                ?,
                ?,
                ?
            )
            """,
            (
                patient_id,
                report_name,
                findings
            )
        )

        conn.commit()

        conn.close()

        return True