import google_auth_httplib2
import httplib2
import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest

SCOPE = "https://www.googleapis.com/auth/spreadsheets"
SPREADSHEET_ID = "1QlPTiVvfRM82snGN6LELpNkOwVI1_Mp9J9xeJe-QoaA"
SHEET_NAME = "Database"
#GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"


@st.experimental_singleton()
def connect_to_gsheet():
    # Create a connection object.
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[SCOPE],
    )

    # Create a new Http() object for every request
    def build_request(http, *args, **kwargs):
        new_http = google_auth_httplib2.AuthorizedHttp(
            credentials, http=httplib2.Http()
        )
        return HttpRequest(new_http, *args, **kwargs)

    authorized_http = google_auth_httplib2.AuthorizedHttp(
        credentials, http=httplib2.Http()
    )
    service = build(
        "sheets",
        "v4",
        requestBuilder=build_request,
        http=authorized_http,
    )
    gsheet_connector = service.spreadsheets()
    return gsheet_connector


def get_data(gsheet_connector) -> pd.DataFrame:
    values = (
        gsheet_connector.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A:E",
        )
        .execute()
    )

    df = pd.DataFrame(values["values"])
    df.columns = df.iloc[0]
    df = df[1:]
    return df


def add_row_to_gsheet(gsheet_connector, row) -> None:
    gsheet_connector.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=f"{SHEET_NAME}!A:E",
        body=dict(values=row),
        valueInputOption="USER_ENTERED",
    ).execute()


st.set_page_config(page_title="Welcome", layout="centered")

st.title("Welcome")

#gsheet_connector = connect_to_gsheet()

#st.sidebar.write(
#    f"This app shows how a Streamlit app can interact easily with a [Google Sheet]({GSHEET_URL}) to read or store data."
#)

st.sidebar.write(
    f"[Read more](https://docs.streamlit.io/knowledge-base/tutorials/databases/public-gsheet) about connecting your Streamlit app to Google Sheets."
)

button = st.button("Volunteer Sign In", key="signInButton", help="Click here to check in for volunteer shift", on_click=None, disabled=False, use_container_width=False)
sign_out_button = st.button("Volunteer Sign Out", key="signOutButton", help="Click here to check out after a volunteer shift", on_click=None, disabled=False, use_container_width=False)
employee_button = st.button("Employee Access", key="employeeButton", help="Click here to access employee information", on_click=None, disabled=False, use_container_width=False)

with button:
    submitted = st.form_submit_button(label="Submit")


if submitted:
    #add_row_to_gsheet(
    #    gsheet_connector,
    #    [[author, bug_type, comment, str(date), bug_severity]],
    #)
    st.success("Success!")
    st.balloons()

#expander = st.expander("See all records")
#with expander:
    #st.write(f"Open original [Google Sheet]({GSHEET_URL})")
    #dataframe(get_data(gsheet_connector))
