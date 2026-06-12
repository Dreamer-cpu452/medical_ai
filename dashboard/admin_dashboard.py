import streamlit as st


class AdminDashboard:

    def show(self):

        st.title(
            "Admin Dashboard"
        )

        st.metric(
            "Total Patients",
            500
        )

        st.metric(
            "Doctors",
            50
        )

        st.metric(
            "Beds Occupied",
            120
        )