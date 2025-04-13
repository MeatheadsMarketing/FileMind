
# filemind/pages/final_output_table.py

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="📦 Final Output Table – Phase 2 Applet 17", layout="wide")
st.title("📦 FILEMIND – Final Output Table")
st.markdown("Preview full routing, tagging, and readiness status across all files.")

registry_path = "/mnt/data/zip_registry.csv"

if not os.path.exists(registry_path):
    st.error("zip_registry.csv not found. Please run earlier steps first.")
    st.stop()

df = pd.read_csv(registry_path)

cols_to_display = [
    "Filename", "Extension", "Size (KB)", "Routing", "Manual Tags",
    "Categorized Intent", "Categorized Role", "System Readiness",
    "Confidence Score", "Cluster Group"
]

st.dataframe(df[cols_to_display], use_container_width=True)

final_map_path = "/mnt/data/zip_filemap.csv"
df.to_csv(final_map_path, index=False)
st.success(f"✅ Full filemap saved to: {final_map_path}")
