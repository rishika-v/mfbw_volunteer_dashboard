import streamlit as st

# read csv of users

# on button click submit, check if valid user

user_input = st.text_input("Enter your name")
food_input = st.text_input("Enter lbs of food")
submit_button = st.button("Submit")

if submit_button:
    user_input