
# filemind/pages/save_bundle_output.py

import streamlit as st
import zipfile
import os

st.set_page_config(page_title="🗂️ Final ZIP Output – Phase 2 Applet 20", layout="wide")
st.title("🗂️ FILEMIND – Final Bundle Output")
st.markdown("Package all metadata, summaries, and filemaps into one ZIP archive for archival or deployment.")

output_name = st.text_input("Name your final archive", value="zip_bundle_final.zip")
output_path = f"/mnt/data/{output_name}"

files_to_bundle = [
    "zip_registry.csv",
    "zip_filemap.csv",
    "file_summaries.csv",
    "zip_shortcut_index.csv",
    "assistant_tag_map.json",
    "zip_audit_report.md",
    "extension_summary.json"
]

if st.button("💾 Save Final Bundle"):
    with zipfile.ZipFile(output_path, 'w') as zipf:
        for file in files_to_bundle:
            full_path = f"/mnt/data/{file}"
            if os.path.exists(full_path):
                zipf.write(full_path, arcname=file)

    st.success(f"✅ Final bundle saved to: {output_path}")
    st.markdown(f"[Download ZIP](sandbox:{output_path})")
