import streamlit as st
import pandas as pd
import os

st.title("AI-Assisted Data Visualization Study")

# Mode selection
mode = st.radio("Select Mode", ["Without AI", "With AI"])

st.write("This is the first version of my research prototype.")

# Participant name
user_name = st.text_input("Enter your name")

# Task instructions
st.write("### Task")
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

if mode == "With AI":
    with col2:
        st.write("### 🤖 AI Suggestions")
        st.info("Trend detected: Energy increases overall with a dip in 2020.")
        st.write("Suggestion: Investigate why 2020 decreased.")
        st.write("### Recommendation")
        st.write("Use the line chart to compare year-to-year changes.")

# Participant response
user_response = st.text_area("Write your insight here:")

# Save response to CSV
file_exists = os.path.isfile("responses.csv")

if st.button("Submit"):
    with open("responses.csv", "a", encoding="utf-8") as f:
        if not file_exists:
            f.write("Name,Mode,Response\n")
        f.write(f"{user_name},{mode},{user_response}\n")
    st.success("Response saved!")