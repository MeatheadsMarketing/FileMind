# app.py
# Launches the correct dashboard file in Streamlit Cloud

import streamlit as st

st.set_page_config(page_title="Redirecting to Dashboard...", layout="centered")
st.success("🔁 Redirecting to FILEMIND dashboard...")
st.switch_page("filemind_dashboard.py")
