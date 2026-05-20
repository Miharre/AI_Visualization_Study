import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import random

st.title("AI-Assisted Data Visualization Study")

# -----------------------------
# Google Sheets connection
# -----------------------------
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)

client = gspread.authorize(creds)

sheet = client.open_by_key(
    "1_1JebkKG-A21WQ_zh_Pt4Kt6P0UMpqQh85zxtZu5wFk"
).sheet1

# -----------------------------
# Random experimental assignment
# -----------------------------
if "mode" not in st.session_state:
    st.session_state.mode = random.choice(["Without AI", "With AI"])

mode = st.session_state.mode

st.write("This study examines how people interpret data visualizations.")

# Participant name
user_name = st.text_input("Enter your name")

# Task instructions
st.write("### Task")
st.write("Please review the data and visualization below, then answer these questions:")
st.write("1. What is the overall trend?")
st.write("2. Which year has the highest value?")
st.write("3. Is there any unusual pattern?")

# Sample data
data = {
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Energy": [100, 150, 130, 170, 200]
}

df = pd.DataFrame(data)

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.write("### Data Preview")
    st.dataframe(df)

    st.write("### Visualization")
    st.line_chart(df.set_index("Year"))

# AI condition only
if mode == "With AI":
    with col2:
        st.write("### 🤖 AI Suggestions")
        st.info("Trend detected: Energy increases overall with a dip in 2020.")
        st.write("Suggestion: Investigate why 2020 decreased.")
        st.write("### Recommendation")
        st.write("Use the line chart to compare year-to-year changes.")

# Participant response
user_response = st.text_area("Write your insight here:")

# Submit to Google Sheets
if st.button("Submit"):
    if user_name.strip() == "" or user_response.strip() == "":
        st.warning("Please enter your name and response before submitting.")
    else:
        sheet.append_row([user_name, mode, user_response])
        st.success("Response saved successfully. Thank you for participating!")