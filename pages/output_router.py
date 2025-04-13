
# filemind/pages/output_router.py

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="🚦 Output Router – Phase 2 Applet 13", layout="wide")
st.title("🚦 FILEMIND – File Output Routing")
st.markdown("Assign routing destinations to files: → Scan, → Export, → Merge, → Archive.")

registry_path = "/mnt/data/zip_registry.csv"

if not os.path.exists(registry_path):
    st.error("zip_registry.csv not found. Please run the File Registry Table applet first.")
    st.stop()

df = pd.read_csv(registry_path)

files = df["Filename"].tolist()
selected_file = st.selectbox("Select file to route", files)
route_option = st.radio("Choose output destination", ["→ Scan", "→ Export", "→ Merge", "→ Archive"])

if "Routing" not in df.columns:
    df["Routing"] = ""

if st.button("Assign Route"):
    df.loc[df["Filename"] == selected_file, "Routing"] = route_option
    df.to_csv(registry_path, index=False)
    st.success(f"✅ Route `{route_option}` assigned to `{selected_file}`")

st.markdown("---")
st.markdown("### Current File Routing Map")
st.dataframe(df[["Filename", "Routing"]], use_container_width=True)
