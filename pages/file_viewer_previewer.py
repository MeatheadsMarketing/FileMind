
# filemind/pages/file_viewer_previewer.py

import streamlit as st
from pathlib import Path
import os

st.set_page_config(page_title="🔍 File Viewer – Phase 2 Applet 11", layout="wide")
st.title("🔍 FILEMIND – File Previewer")
st.markdown("Preview contents of files before classification or export.")

workspace_root = Path("/mnt/data/filemind_zip_workspace/extracted")

if not workspace_root.exists():
    st.error("Extracted folder not found. Please run ZIP Loader first.")
    st.stop()

target_files = []
for root, _, files in os.walk(workspace_root):
    for name in files:
        full_path = Path(root) / name
        rel_path = full_path.relative_to(workspace_root)
        if full_path.suffix.lower() in [".txt", ".md", ".json", ".csv"]:
            target_files.append((str(rel_path), str(full_path)))

file_selection = st.selectbox("Choose file to preview", [f[0] for f in target_files])
selected_path = dict(target_files).get(file_selection)

if selected_path:
    st.markdown(f"### Preview of `{file_selection}`")
    try:
        with open(selected_path, "r", encoding="utf-8") as f:
            content = f.read()
            st.code(content[:3000], language="markdown")
    except Exception as e:
        st.error(f"❌ Unable to preview file: {e}")
