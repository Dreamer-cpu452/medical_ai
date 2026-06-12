import streamlit as st


class DoctorDashboard:

    def show(self):

        st.title(
            "Doctor Dashboard"
        )

        st.metric(
            "Today's Patients",
            15
        )

        st.metric(
            "Pending Reports",
            4
        )

        st.metric(
            "Appointments",
            20
        )