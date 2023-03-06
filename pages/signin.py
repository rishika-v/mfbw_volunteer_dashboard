import streamlit as st
import requests
import json
import pandas as pd
from datetime import datetime

# get list of users as json file?

api_url = ?

users = pd.read_json("?")
user_names = users["Name"]
user_input = st.selectbox(label="Please enter your name", options = user_names)
check_in_button = st.button("Check in")

if check_in_button:

    todo = {"id": user_input, "start": datetime.now()}
    response = requests.post(api_url, json=todo)


    # API call to create shift, inputting user object
    st.write("Check in successful!")