import streamlit as st


class UserProfile:

    def show_profile(
        self,
        user
    ):

        st.subheader(
            "User Profile"
        )

        st.write(
            f"Name : {user[1]}"
        )

        st.write(
            f"Email : {user[2]}"
        )

        st.write(
            f"Role : {user[4]}"
        )