
import sqlite3
import os

# Create database folder
os.makedirs("database", exist_ok=True)

# Connect Database
conn = sqlite3.connect(
    "database/healthcare.db"
)

cursor = conn.cursor()

# --------------------------------
# USERS TABLE
# --------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

# --------------------------------
# PATIENTS TABLE
# --------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    age INTEGER,
    gender TEXT,
    blood_group TEXT,
    phone TEXT
)
""")

# --------------------------------
# DOCTORS TABLE
# --------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors(
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_name TEXT,
    specialization TEXT,
    department TEXT,
    experience INTEGER
)
""")

# --------------------------------
# APPOINTMENTS TABLE
# --------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments(
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    appointment_date TEXT,
    status TEXT
)
""")

# --------------------------------
# PRESCRIPTIONS TABLE
# --------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS prescriptions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    medicine TEXT,
    dosage TEXT
)
""")

# --------------------------------
# REPORTS TABLE
# --------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS reports(
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    report_name TEXT,
    findings TEXT
)
""")

# --------------------------------
# DIAGNOSTIC REPORTS TABLE
# --------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS diagnostic_reports(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    report_name TEXT,
    findings TEXT
)
""")

# --------------------------------
# SAVE CHANGES
# --------------------------------

conn.commit()

print(
    "Healthcare Database Created Successfully"
)

conn.close()

