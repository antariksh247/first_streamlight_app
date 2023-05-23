import streamlit as st

def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username == "admin" and password == "password":
            st.success("Logged in successfully!")
            # Redirect to the new page
            new_page()
        else:
            st.error("Invalid username or password.")

def new_page():
    st.title("Welcome to the New Page!")
    st.write("This is the new page content.")

# Initially display the login page
login()
