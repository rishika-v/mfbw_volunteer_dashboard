import streamlit as st

# read csv of users

# on button click submit, check if valid user

user_input = st.text_input("Please enter your user id", placeholder="Please enter your user id")
check_in_button = st.button("Check in")

if check_in_button:
    user_input