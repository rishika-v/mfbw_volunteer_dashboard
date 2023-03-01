import streamlit as st


user_input = st.text_input("Enter your name")
food_input = st.text_input("Enter lbs of food")
submit_button = st.button("Submit")

if submit_button:
    st.write("Check out successful!")
    #foodAmt = float(food_input) if food_input.isnumeric() else st.write("Please input a number")
    # API call to read DB and find user object aligned with that name
    # if that doesn't exist, say no
    #currentShift = user.shiftsWorked[-1]
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