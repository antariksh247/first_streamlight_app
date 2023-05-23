import streamlit as st

def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username == "admin" and password == "password":
            st.success("Logged in successfully!")
            # Add your code for the logged-in page or redirect to another page
        else:
            st.error("Invalid username or password.")

login()
