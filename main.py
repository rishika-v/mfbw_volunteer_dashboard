import streamlit as st
import numpy as np
import pandas as pd

from streamlit.components.v1 import html

st.set_page_config(layout="centered", page_icon="🍏", page_title="Bmore Food Volunteer Portal")

st.markdown("<h1 style='text-align: center; color: green;'>Bmore Food Volunteer Portal</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Welcome!</h2>", unsafe_allow_html=True)
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


col1,col2,col3,col4=st.columns([0.3,1.5,1.5,1.5])
with col1:
    placeholder = st.empty
with col2:
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        box-shadow: 0px 10px 14px -7px #3e7327;
        background:linear-gradient(to bottom, #77b55a 5%, #72b352 100%);
        background-color:#77b55a;
        border-radius:4px;
        border:1px solid #4b8f29;
        display:inline-block;
        cursor:pointer;
        color:#ffffff;
        font-family:Arial;
        font-size:13px;
        font-weight:bold;
        padding:6px 12px;
        text-decoration:none;
        text-shadow:0px 1px 0px #5b8a3c;
        height: 5em;
        width: 15em;
        }
        </style>""", unsafe_allow_html=True)
    sign_in_button = st.button("Volunteer Sign In", key="signInButton")
    if sign_in_button:
        nav_page("signin")
with col3:
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        box-shadow: 0px 10px 14px -7px #3e7327;
        background:linear-gradient(to bottom, #77b55a 5%, #72b352 100%);
        background-color:#77b55a;
        border-radius:4px;
        border:1px solid #4b8f29;
        display:inline-block;
        cursor:pointer;
        color:#ffffff;
        font-family:Arial;
        font-size:13px;
        font-weight:bold;
        padding:6px 12px;
        text-decoration:none;
        text-shadow:0px 1px 0px #5b8a3c;
        height: 5em;
        width: 15em;
        }
        </style>""", unsafe_allow_html=True)
    sign_out_button = st.button("Volunteer Sign Out", key="signOutButton")
    if sign_out_button:
        nav_page("signout")
with col4:
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        box-shadow: 0px 10px 14px -7px #3e7327;
        background:linear-gradient(to bottom, #77b55a 5%, #72b352 100%);
        background-color:#77b55a;
        border-radius:4px;
        border:1px solid #4b8f29;
        display:inline-block;
        cursor:pointer;
        color:#ffffff;
        font-family:Arial;
        font-size:13px;
        font-weight:bold;
        padding:6px 12px;
        text-decoration:none;
        text-shadow:0px 1px 0px #5b8a3c;
        height: 5em;
        width: 15em;
        }
        </style>""", unsafe_allow_html=True)
    employee_button = st.button("Employee Access", key="employeeButton")
    if employee_button:
        nav_page("employee")




