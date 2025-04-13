
# filemind/pages/summary_table_generator.py

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="📋 Summary Table – Phase 2 Applet 14", layout="wide")
st.title("📋 FILEMIND – Summary Table Generator")
st.markdown("Generate a table of GPT-style summaries for selected files.")

registry_path = "/mnt/data/zip_registry.csv"
output_path = "/mnt/data/file_summaries.csv"

if not os.path.exists(registry_path):
    st.error("Registry not found. Please run earlier applets.")
    st.stop()

df = pd.read_csv(registry_path)
text_files = df[df["Extension"].isin([".txt", ".md", ".json"])]

selected = st.multiselect("Choose files to summarize", text_files["Filename"].tolist())

if selected:
    st.info("Simulating GPT summary block. (Replace with OpenAI call if desired)")
    summaries = []
    for fname in selected:
        row = text_files[text_files["Filename"] == fname].iloc[0]
        summaries.append({
            "Filename": row["Filename"],
            "Summary": f"This file contains structured logic and was tagged for role '{row.get('Categorized Role', 'N/A')}'.",
            "Detected Shortcuts": "#X, #S1" if "scan" in row.get("Categorized Intent", "").lower() else "",
            "Vibe Score": 8.5
        })

    df_summary = pd.DataFrame(summaries)
    st.dataframe(df_summary, use_container_width=True)
    df_summary.to_csv(output_path, index=False)
    st.success(f"✅ Saved to: {output_path}")
else:
    st.warning("Select files to generate summary.")
