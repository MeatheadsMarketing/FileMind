
# filemind/pages/extension_summary_chart.py

import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(page_title="📊 Extension Summary – Phase 2 Applet 6", layout="wide")
st.title("📊 FILEMIND – File Extension Summary")
st.markdown("Visualize filetype breakdown from extracted archive.")

registry_path = "/mnt/data/zip_registry.csv"
if not os.path.exists(registry_path):
    st.error("Registry not found. Please run the File Registry Table applet first.")
    st.stop()

df = pd.read_csv(registry_path)
ext_counts = df["Extension"].value_counts().reset_index()
ext_counts.columns = ["Extension", "Count"]

fig = px.pie(ext_counts, names="Extension", values="Count", title="File Type Distribution")
st.plotly_chart(fig, use_container_width=True)

summary_path = "/mnt/data/extension_summary.json"
ext_counts.to_json(summary_path, orient="records", indent=2)
st.success(f"Saved summary to: {summary_path}")
