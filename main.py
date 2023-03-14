import streamlit as st
import numpy as np
import pandas as pd

from streamlit.components.v1 import html

st.set_page_config(layout="centered", page_icon="🍏", page_title="Bmore Food Volunteer Portal")
st.markdown("<h1 style='text-align: center; color: green;'>Bmore Food Volunteer Portal</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Welcome! Please log in/log out</h2>", unsafe_allow_html=True)
unsafe_allow_html = True

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

st.markdown(""" <style> div.stButton > button:first-child {
    background-color: rgb(204, 49, 49);
    } </style>""", unsafe_allow_html=True)





col1,col2,col3=st.columns([0.3,1.2,0.3])
with col1:
    sign_in_button = st.button("Volunteer Sign In", key="signInButton", help="Click here to check in for volunteer shift", on_click=None, disabled=False)
    if sign_in_button:
        nav_page("signin")
with col2:
    sign_out_button = st.button("Volunteer Sign Out", key="signOutButton", help="Click here to check out after a volunteer shift", on_click=None, disabled=False)
    if sign_out_button:
        nav_page("signout")
with col3:
    employee_button = st.button("Employee Access", key="employeeButton", help="Click here to access employee information", on_click=None, disabled=False)
    if employee_button:
        nav_page("employee")




