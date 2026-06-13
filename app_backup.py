import pandas as pd
import plotly.express as px
import streamlit as st

from authentication.register import UserRegister
from authentication.login import UserLogin

from patient_management.patient_registration import PatientRegistration
from patient_management.patient_history import PatientHistory

from doctor_management.doctor_registration import DoctorRegistration
from doctor_management.doctor_dashboard import DoctorDashboard as DoctorManagementDashboard

from appointment_management.appointment_booking import AppointmentBooking

from ehr_system.prescriptions import PrescriptionManager
from ehr_system.diagnostic_reports import DiagnosticReports

from ai_prediction.disease_prediction import DiseasePrediction
from doctor_management.treatment_recommendation import TreatmentRecommendation

from treatment_engine.treatment_plan import TreatmentPlan
from treatment_engine.specialist_recommendation import SpecialistRecommendation
from treatment_engine.diagnostic_test_recommendation import DiagnosticTestRecommendation
from treatment_engine.medication_guidance import MedicationGuidance

from outcome_prediction.recovery_prediction import RecoveryPrediction
from outcome_prediction.icu_prediction import ICUPrediction
from outcome_prediction.mortality_prediction import MortalityPrediction
from outcome_prediction.hospital_stay_prediction import HospitalStayPrediction

from bed_management.bed_tracking import BedTracking

from staff_management.staff_prediction import StaffPrediction

from resource_management.resource_forecasting import ResourceForecasting

from report_analysis.blood_report_analysis import BloodReportAnalysis

from emergency_system.alert_engine import AlertEngine
from chatbot.chatbot import HealthcareChatbot

from dashboard.patient_dashboard import PatientDashboard
from dashboard.doctor_dashboard import DoctorDashboard
from dashboard.admin_dashboard import AdminDashboard

from dashboard.analytics import Analytics

from reports.disease_statistics import DiseaseStatistics
from reports.resource_report import ResourceReport
from reports.occupancy_report import OccupancyReport
from reports.doctor_performance import DoctorPerformance
from reports.recovery_report import RecoveryReport



# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Healthcare System",
    page_icon="🏥",
    layout="wide"
)

# -----------------------------------
# OBJECTS
# -----------------------------------

register_obj = UserRegister()
login_obj = UserLogin()

patient_obj = PatientRegistration()
patient_history = PatientHistory()

doctor_obj = DoctorRegistration()
doctor_dashboard = DoctorManagementDashboard()

appointment_obj = AppointmentBooking()

prescription_obj = PrescriptionManager()
report_obj = DiagnosticReports()

prediction_obj = DiseasePrediction()
treatment_obj = TreatmentRecommendation()

treatment_plan = TreatmentPlan()
specialist_obj = SpecialistRecommendation()
test_obj = DiagnosticTestRecommendation()
medication_obj = MedicationGuidance()

recovery_obj = RecoveryPrediction()
icu_obj = ICUPrediction()
mortality_obj = MortalityPrediction()
stay_obj = HospitalStayPrediction()

bed_obj = BedTracking()

staff_obj = StaffPrediction()

resource_obj = ResourceForecasting()

report_analysis_obj = BloodReportAnalysis()

alert_obj = AlertEngine()
chatbot_obj = HealthcareChatbot()

patient_dashboard_obj = PatientDashboard()
doctor_dashboard_obj = DoctorDashboard()
admin_dashboard_obj = AdminDashboard()

analytics_obj = Analytics()

disease_stats_obj = DiseaseStatistics()
resource_report_obj = ResourceReport()
occupancy_report_obj = OccupancyReport()
doctor_performance_obj = DoctorPerformance()
recovery_report_obj = RecoveryReport()
# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("🏥 AI Healthcare System")

menu = [
    "Home",
    "Authentication",
    "Patient Management",
    "Doctor Management",
    "Appointment Management",
    "EHR System",
    "AI Prediction",
    "Treatment Engine",
    "Outcome Prediction",
    "Bed Management",
    "Staff Management",
    "Resource Management",
    "Report Analysis",
    "Emergency System",
    "Chatbot",
    "Dashboard",
    "Analytics",
    "Reports"
]

choice = st.sidebar.selectbox(
    "Select Module",
    menu
)

# -----------------------------------
# HOME
# -----------------------------------

if choice == "Home":

    st.title(
        "AI-Powered Healthcare Prediction & Resource Management System"
    )

    st.success(
        "System Running Successfully"
    )

# -----------------------------------
# AUTHENTICATION
# -----------------------------------

elif choice == "Authentication":

    st.header("Authentication")

    auth_option = st.radio(
        "Select",
        [
            "Register",
            "Login"
        ]
    )

    if auth_option == "Register":

        full_name = st.text_input(
            "Full Name"
        )

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        role = st.selectbox(
            "Role",
            [
                "Patient",
                "Doctor",
                "Admin"
            ]
        )

        if st.button("Register"):

            result = register_obj.register_user(
                full_name,
                email,
                password,
                role
            )

            if result:

                st.success(
                    "Registration Successful"
                )

            else:

                st.error(
                    "User Already Exists"
                )

    else:

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            user = login_obj.login(
                email,
                password
            )

            if user:

                st.success(
                    f"Welcome {user[1]}"
                )

            else:

                st.error(
                    "Invalid Credentials"
                )

# -----------------------------------
# PATIENT MANAGEMENT
# -----------------------------------

elif choice == "Patient Management":

    st.header(
        "Patient Management"
    )

    name = st.text_input(
        "Patient Name"
    )

    age = st.number_input(
        "Age",
        min_value=0
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )

    blood_group = st.text_input(
        "Blood Group"
    )

    phone = st.text_input(
        "Phone"
    )

    if st.button(
        "Add Patient"
    ):

        result = patient_obj.add_patient(
            name,
            age,
            gender,
            blood_group,
            phone
        )

        if result:

            st.success(
                "Patient Added Successfully"
            )

    st.subheader(
        "Patient Records"
    )

    st.write(
        patient_history.get_all_patients()
    )

# -----------------------------------
# DOCTOR MANAGEMENT
# -----------------------------------

elif choice == "Doctor Management":

    st.header(
        "Doctor Management"
    )

    doctor_name = st.text_input(
        "Doctor Name"
    )

    specialization = st.text_input(
        "Specialization"
    )

    department = st.text_input(
        "Department"
    )

    experience = st.number_input(
        "Experience",
        min_value=0
    )

    if st.button(
        "Add Doctor"
    ):

        result = doctor_obj.add_doctor(
            doctor_name,
            specialization,
            department,
            experience
        )

        if result:

            st.success(
                "Doctor Added Successfully"
            )

    st.subheader(
        "Doctors"
    )

    st.write(
        doctor_dashboard.get_doctors()
    )

# -----------------------------------
# APPOINTMENT MANAGEMENT
# -----------------------------------

elif choice == "Appointment Management":

    st.header(
        "Appointment Booking"
    )

    patient_id = st.number_input(
        "Patient ID",
        min_value=1
    )

    doctor_id = st.number_input(
        "Doctor ID",
        min_value=1
    )

    appointment_date = st.text_input(
        "Appointment Date"
    )

    if st.button(
        "Book Appointment"
    ):

        result = appointment_obj.book_appointment(
            patient_id,
            doctor_id,
            appointment_date
        )

        if result:

            st.success(
                "Appointment Booked Successfully"
            )

# -----------------------------------
# EHR SYSTEM
# -----------------------------------

elif choice == "EHR System":

    st.header(
        "Electronic Health Records"
    )

    ehr_option = st.selectbox(
        "Select",
        [
            "Prescription",
            "Diagnostic Report"
        ]
    )

    if ehr_option == "Prescription":

        patient_id = st.number_input(
            "Patient ID",
            min_value=1
        )

        doctor_id = st.number_input(
            "Doctor ID",
            min_value=1
        )

        medicine = st.text_input(
            "Medicine"
        )

        dosage = st.text_input(
            "Dosage"
        )

        if st.button(
            "Save Prescription"
        ):

            prescription_obj.add_prescription(
                patient_id,
                doctor_id,
                medicine,
                dosage
            )

            st.success(
                "Prescription Saved"
            )

    else:

        patient_id = st.number_input(
            "Patient ID",
            min_value=1
        )

        report_name = st.text_input(
            "Report Name"
        )

        findings = st.text_area(
            "Findings"
        )

        if st.button(
            "Save Report"
        ):

            report_obj.add_report(
                patient_id,
                report_name,
                findings
            )

            st.success(
                "Report Saved"
            )

# -----------------------------------
# AI PREDICTION
# -----------------------------------

elif choice == "AI Prediction":

    st.header(
        "Disease Prediction"
    )

    disease = st.selectbox(
        "Select Disease",
        [
            "Diabetes",
            "Heart Disease",
            "Kidney Disease",
            "Cancer"
        ]
    )

    if disease == "Diabetes":

        age = st.number_input("Age")
        bmi = st.number_input("BMI")
        glucose = st.number_input("Glucose")

        if st.button("Predict"):

            result = prediction_obj.predict_diabetes(
                age,
                bmi,
                glucose
            )

            st.success(result)

    elif disease == "Heart Disease":

        age = st.number_input("Age")
        cholesterol = st.number_input("Cholesterol")
        bp = st.number_input("Blood Pressure")

        if st.button("Predict"):

            result = prediction_obj.predict_heart(
                age,
                cholesterol,
                bp
            )

            st.success(result)

    elif disease == "Kidney Disease":

        age = st.number_input("Age")
        creatinine = st.number_input("Creatinine")
        urea = st.number_input("Blood Urea")

        if st.button("Predict"):

            result = prediction_obj.predict_kidney(
                age,
                creatinine,
                urea
            )

            st.success(result)

    else:

        age = st.number_input("Age")
        tumor_size = st.number_input("Tumor Size")
        smoking_years = st.number_input("Smoking Years")

        if st.button("Predict"):

            result = prediction_obj.predict_cancer(
                age,
                tumor_size,
                smoking_years
            )

            st.success(result)
# -----------------------------------
# TREATMENT ENGINE
# -----------------------------------

elif choice == "Treatment Engine":

    st.header("Treatment Engine")

    disease = st.selectbox(
        "Disease",
        [
            "Diabetes",
            "Heart Disease",
            "Kidney Disease",
            "Cancer"
        ]
    )

    st.subheader("Treatment Plan")

    st.write(
        treatment_plan.generate_plan(
            disease
        )
    )

    st.subheader("Specialist")

    st.success(
        specialist_obj.recommend(
            disease
        )
    )

    st.subheader("Tests")

    st.write(
        test_obj.recommend_tests(
            disease
        )
    )

    st.subheader("Medication Guidance")

    st.info(
        medication_obj.get_guidance(
            disease
        )
    )

# -----------------------------------
# OUTCOME PREDICTION
# -----------------------------------

elif choice == "Outcome Prediction":

    st.header(
        "Outcome Prediction"
    )

    age = st.number_input(
        "Age",
        min_value=1
    )

    severity = st.slider(
        "Severity",
        1,
        10
    )

    oxygen = st.slider(
        "Oxygen Level",
        50,
        100
    )

    if st.button(
        "Predict Outcome"
    ):

        st.success(
            f"Recovery Score : {recovery_obj.predict(age,severity)}"
        )

        st.warning(
            f"ICU Risk : {icu_obj.predict(oxygen)}"
        )

        st.error(
            f"Mortality Risk : {mortality_obj.predict(age,severity)}"
        )

        st.info(
            f"Hospital Stay : {stay_obj.predict_days(severity)} Days"
        )

# -----------------------------------
# BED MANAGEMENT
# -----------------------------------

elif choice == "Bed Management":

    st.header(
        "Bed Management"
    )

    total = st.number_input(
        "Total Beds",
        min_value=1
    )

    occupied = st.number_input(
        "Occupied Beds",
        min_value=0
    )

    if st.button(
        "Check Availability"
    ):

        st.success(
            f"Available Beds : {bed_obj.available_beds(total,occupied)}"
        )

# -----------------------------------
# STAFF MANAGEMENT
# -----------------------------------

elif choice == "Staff Management":

    st.header(
        "Staff Requirement Prediction"
    )

    patients = st.number_input(
        "Number Of Patients",
        min_value=1
    )

    if st.button(
        "Predict Staff"
    ):

        st.success(
            f"Required Staff : {staff_obj.predict_needed(patients)}"
        )

# -----------------------------------
# RESOURCE MANAGEMENT
# -----------------------------------

elif choice == "Resource Management":

    st.header(
        "Resource Forecasting"
    )

    usage = st.number_input(
        "Current Resource Usage",
        min_value=1
    )

    if st.button(
        "Forecast"
    ):

        st.success(
            f"Expected Requirement : {resource_obj.forecast(usage)}"
        )

# -----------------------------------
# REPORT ANALYSIS
# -----------------------------------

elif choice == "Report Analysis":

    st.header(
        "Blood Report Analysis"
    )

    hb = st.number_input(
        "Hemoglobin"
    )

    sugar = st.number_input(
        "Sugar"
    )

    if st.button(
        "Analyze"
    ):

        st.write(
            report_analysis_obj.analyze(
                hb,
                sugar
            )
        )

# -----------------------------------
# EMERGENCY SYSTEM
# -----------------------------------

elif choice == "Emergency System":

    st.header(
        "Emergency Alert System"
    )

    oxygen = st.slider(
        "Oxygen Level",
        50,
        100
    )

    if st.button(
        "Generate Alert"
    ):

        st.error(
            alert_obj.generate_alert(
                oxygen
            )
        )
# -----------------------------------
# CHATBOT
# -----------------------------------

elif choice == "Chatbot":

    st.header("AI Healthcare Chatbot")

    message = st.text_input(
        "Ask Something"
    )

    if st.button(
        "Send"
    ):

        response = chatbot_obj.reply(
            message
        )

        st.success(
            response
        )

# -----------------------------------
# DASHBOARD
# -----------------------------------

elif choice == "Dashboard":

    st.header(
        "Dashboard"
    )

    dashboard_type = st.selectbox(
        "Select Dashboard",
        [
            "Patient",
            "Doctor",
            "Admin"
        ]
    )

    if dashboard_type == "Patient":

        patient_dashboard_obj.show()

    elif dashboard_type == "Doctor":

        doctor_dashboard_obj.show()

    else:

        admin_dashboard_obj.show()

# -----------------------------------
# ANALYTICS
# -----------------------------------

elif choice == "Analytics":

    st.header("Healthcare Analytics Dashboard")

    data = analytics_obj.summary()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Patients", data["Patients"])

    with col2:
        st.metric("Doctors", data["Doctors"])

    with col3:
        st.metric("Appointments", data["Appointments"])

    df = pd.DataFrame({
        "Category": [
            "Patients",
            "Doctors",
            "Appointments"
        ],
        "Count": [
            data["Patients"],
            data["Doctors"],
            data["Appointments"]
        ]
    })

    fig = px.bar(
        df,
        x="Category",
        y="Count",
        title="Healthcare Overview"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------------
# REPORTS
# -----------------------------------

elif choice == "Reports":

    st.header("Healthcare Reports")

    report_type = st.selectbox(
        "Select Report",
        [
            "Disease Statistics",
            "Resource Report",
            "Occupancy Report",
            "Doctor Performance",
            "Recovery Report"
        ]
    )

    if report_type == "Disease Statistics":

        data = disease_stats_obj.generate()

        df = pd.DataFrame(
            list(data.items()),
            columns=[
                "Disease",
                "Patients"
            ]
        )

        st.dataframe(df)

        fig = px.pie(
            df,
            names="Disease",
            values="Patients",
            title="Disease Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    elif report_type == "Resource Report":

        data = resource_report_obj.generate()

        df = pd.DataFrame(
            list(data.items()),
            columns=[
                "Resource",
                "Count"
            ]
        )

        st.dataframe(df)

        fig = px.bar(
            df,
            x="Resource",
            y="Count",
            title="Hospital Resources"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    elif report_type == "Occupancy Report":

        data = occupancy_report_obj.generate()

        df = pd.DataFrame(
            list(data.items()),
            columns=[
                "Status",
                "Beds"
            ]
        )

        fig = px.pie(
            df,
            names="Status",
            values="Beds",
            title="Bed Occupancy"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    elif report_type == "Doctor Performance":

        st.json(
            doctor_performance_obj.generate()
        )

    else:

        data = recovery_report_obj.generate()

        df = pd.DataFrame(
            list(data.items()),
            columns=[
                "Status",
                "Patients"
            ]
        )

        fig = px.bar(
            df,
            x="Status",
            y="Patients",
            title="Recovery Report"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )