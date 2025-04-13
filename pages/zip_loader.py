
# filemind/pages/zip_loader.py

import streamlit as st
import zipfile
import os
import shutil
from pathlib import Path

st.set_page_config(page_title="📦 ZIP Loader – Phase 2 Applet 1", layout="wide")
st.title("📦 FILEMIND – ZIP Loader")
st.markdown("Upload and extract your data archive for downstream classification and analysis.")

st.header("Step 1: Upload ZIP")
uploaded_zip = st.file_uploader("Upload a .zip file", type="zip")

workspace_dir = Path("/mnt/data/filemind_zip_workspace")
extracted_dir = workspace_dir / "extracted"
workspace_dir.mkdir(parents=True, exist_ok=True)
extracted_dir.mkdir(parents=True, exist_ok=True)

if uploaded_zip:
    zip_path = workspace_dir / uploaded_zip.name
    with open(zip_path, "wb") as f:
        f.write(uploaded_zip.read())

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extracted_dir)

    st.success(f"✅ Extracted to: {extracted_dir}")
    st.session_state["zip_extracted"] = True

    st.markdown("### 📁 Extracted Files:")
    for root, dirs, files in os.walk(extracted_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, extracted_dir)
            size_kb = os.path.getsize(full_path) / 1024
            st.write(f"- `{rel_path}` ({size_kb:.1f} KB)")

if st.button("🔄 Reset Workspace"):
    shutil.rmtree(extracted_dir, ignore_errors=True)
    extracted_dir.mkdir(parents=True, exist_ok=True)
    st.success("Workspace reset.")
