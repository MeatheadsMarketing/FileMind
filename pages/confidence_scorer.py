
# filemind/pages/confidence_scorer.py

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="🔍 Confidence Scorer – Phase 2 Applet 15", layout="wide")
st.title("🔍 FILEMIND – File Confidence Scorer")
st.markdown("Score files based on size, metadata richness, and routing status.")

registry_path = "/mnt/data/zip_registry.csv"

if not os.path.exists(registry_path):
    st.error("zip_registry.csv not found. Please run File Registry Table first.")
    st.stop()

df = pd.read_csv(registry_path)

def score_row(row):
    score = 50
    if row.get("Size (KB)", 0) > 500:
        score += 10
    if row.get("Routing") in ["→ Scan", "→ Merge"]:
        score += 15
    if pd.notna(row.get("Categorized Intent")):
        score += 10
    if pd.notna(row.get("Manual Tags")) and row["Manual Tags"] != "":
        score += 5
    return min(score, 100)

df["Confidence Score"] = df.apply(score_row, axis=1)
df.to_csv(registry_path, index=False)
st.dataframe(df[["Filename", "Size (KB)", "Routing", "Confidence Score"]], use_container_width=True)
st.success("✅ Confidence scores updated.")
