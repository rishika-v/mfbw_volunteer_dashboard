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
food_input = st.text_input("Enter lbs of food")
submit_button = st.button("Submit")

if submit_button:
    st.write("Check out successful!")
    foodAmt = float(food_input) if food_input.isnumeric() else st.write("Please input a number")
    # API call to read DB and find user object aligned with that name
    # if that doesn't exist, say no
    name = user_input
    shifts = users[name]["shiftsWorked"] # access the list of shiftsWorked for that user with name=name
    currentShift = shifts[-1]
    #if (currentShift.end == None ):
        #if (foodAmt >= 0 & foodAmt <=20):
            #currentShift.foodTaken = foodAmt
            # API call to set currentShift.foodTaken = foodAmt
            #currentShift.end = DateTime.now()
            #API write updates for currentShift to DB
            #st.write("Check out successful!")
        #else:
            #st.write("Enter a value between 0 and 20.")
    #else:
        #st.write("No shift started")