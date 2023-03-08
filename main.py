import streamlit as st
import numpy as np
import pandas as pd

from streamlit.components.v1 import html

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


st.title("Welcome to BMore Food!")
sign_in_button = st.button("Sign In", key="signInButton", help="Click here to check in for volunteer shift", on_click=None, disabled=False)
sign_out_button = st.button("Sign Out", key="signOutButton", help="Click here to check out after a volunteer shift", on_click=None, disabled=False)

if sign_in_button:
    nav_page("signin")

if sign_out_button:
    nav_page("signout")