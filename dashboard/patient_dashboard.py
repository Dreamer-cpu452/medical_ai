import streamlit as st


class PatientDashboard:

    def show(self):

        st.title(
            "Patient Dashboard"
        )

        st.metric(
            "Appointments",
            5
        )

        st.metric(
            "Reports",
            12
        )

        st.metric(
            "Prescriptions",
            8
        )