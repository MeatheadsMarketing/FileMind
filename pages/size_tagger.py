
# filemind/pages/size_tagger.py

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="📏 Size Tagger – Phase 2 Applet 4", layout="wide")
st.title("📏 FILEMIND – Size Tier Tagger")
st.markdown("Automatically classify files by size tier.")

registry_path = "/mnt/data/zip_registry.csv"
if not os.path.exists(registry_path):
    st.error("Registry not found. Please run the File Registry Table applet first.")
    st.stop()

df = pd.read_csv(registry_path)

def tag_size_kb(size):
    if size < 10:
        return "Tiny"
    elif size < 100:
        return "Small"
    elif size < 1000:
        return "Medium"
    elif size < 10000:
        return "Large"
    else:
        return "Huge"

df["Size Tier"] = df["Size (KB)"].apply(tag_size_kb)
st.dataframe(df, use_container_width=True)
df.to_csv(registry_path, index=False)
st.success("✅ Size tiers applied and saved to registry.")
