import streamlit as st
import numpy as np
import pandas as pd

from streamlit.components.v1 import html
from streamlit_extras.switch_page_button import switch_page

from .. import extra


@extra
def switch_page(page_name: str):
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("main.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")


def example():
    want_to_contribute = st.button("I want to contribute!")
    if want_to_contribute:
        switch_page("Contribute")


def test_switch_page():
    import pytest
    from streamlit.runtime.scriptrunner import RerunException

    with pytest.raises(RerunException):
        switch_page("streamlit app")


def test_switch_invalid_page():
    import pytest

    with pytest.raises(ValueError):
        switch_page("non existent page")


__title__ = "Switch page function"
__desc__ = "Function to switch page programmatically in a MPA"
__icon__ = "🖱️"
__examples__ = [example]
__author__ = "Zachary Blackwood"
__tests__ = [test_switch_page, test_switch_invalid_page]

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

sign_in_button = st.button("Volunteer Sign In", key="signInButton", help="Click here to check in for volunteer shift", on_click=None, disabled=False, use_container_width=False)
sign_out_button = st.button("Volunteer Sign Out", key="signOutButton", help="Click here to check out after a volunteer shift", on_click=None, disabled=False, use_container_width=False)
employee_button = st.button("Employee Access", key="employeeButton", help="Click here to access employee information", on_click=None, disabled=False, use_container_width=False)

if sign_in_button:
    switch_page("signin")

if sign_out_button:
    switch_page("signout")

if employee_button:
    switch_page("employee")
