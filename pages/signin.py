import streamlit as st


user_input = st.text_input("Please enter your user id", placeholder="Please enter your user id")
check_in_button = st.button("Check in")

if check_in_button:

    # API call to read DB and find user object aligned with that name
    # if that doesn't exist, say no

    # API call to create shift, inputting user object
    st.write("Check in successful!")