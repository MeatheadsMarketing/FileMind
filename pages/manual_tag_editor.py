
# filemind/pages/manual_tag_editor.py

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="🏷️ Manual Tag Editor – Phase 2 Applet 9", layout="wide")
st.title("🏷️ FILEMIND – Manual Tag Editor")
st.markdown("Assign custom tags to one or more files from your archive registry.")

registry_path = "/mnt/data/zip_registry.csv"

if not os.path.exists(registry_path):
    st.error("zip_registry.csv not found. Please run File Registry Table first.")
    st.stop()

registry = pd.read_csv(registry_path)

selected_files = st.multiselect("Select files to tag", registry["Filename"].tolist())
custom_tag = st.text_input("Enter a new tag to apply")

if selected_files and custom_tag:
    tag_col = "Manual Tags"
    if tag_col not in registry.columns:
        registry[tag_col] = ""

    for file in selected_files:
        existing = registry.loc[registry["Filename"] == file, tag_col].values[0]
        updated = ", ".join(sorted(set((existing + ", " + custom_tag).split(", "))))
        registry.loc[registry["Filename"] == file, tag_col] = updated.strip(", ")

    registry.to_csv(registry_path, index=False)
    st.success(f"✅ Applied tag `{custom_tag}` to selected files.")
    st.dataframe(registry[registry["Filename"].isin(selected_files)], use_container_width=True)
else:
    st.info("Select files and input a tag to apply changes.")
