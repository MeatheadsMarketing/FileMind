
# filemind/pages/gpt_export_identifier.py

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="🧠 GPT Export Identifier – Phase 2 Applet 5", layout="wide")
st.title("🧠 FILEMIND – GPT Export Identifier")
st.markdown("Detect if this file bundle was generated from a ChatGPT data export.")

registry_path = "/mnt/data/zip_registry.csv"
if not os.path.exists(registry_path):
    st.error("Registry not found. Please run the File Registry Table applet first.")
    st.stop()

df = pd.read_csv(registry_path)
pattern_matches = df["Filename"].str.contains("conversation-\d{4}-\d{2}-\d{2}", case=False, regex=True)
df["GPT Export Detected"] = pattern_matches

st.dataframe(df, use_container_width=True)
df.to_csv(registry_path, index=False)
st.success("✅ Updated GPT Export detection flags in registry.")
