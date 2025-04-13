
# filemind/pages/directory_visualizer.py

import streamlit as st
import os
from pathlib import Path

st.set_page_config(page_title="📂 Directory Visualizer – Phase 2 Applet 2", layout="wide")
st.title("📂 FILEMIND – Directory Visualizer")
st.markdown("Render and explore folder structure from extracted ZIP.")

workspace_root = Path("/mnt/data/filemind_zip_workspace/extracted")

if not workspace_root.exists():
    st.warning("No extracted files found. Please upload a ZIP first using the ZIP Loader.")
    st.stop()

def render_tree(base_path, level=0):
    for entry in sorted(base_path.iterdir()):
        indent = "&nbsp;" * 4 * level
        if entry.is_dir():
            st.markdown(f"{indent}📁 **{entry.name}/**")
            render_tree(entry, level + 1)
        else:
            size_kb = entry.stat().st_size / 1024
            st.markdown(f"{indent}📄 `{entry.name}` ({size_kb:.1f} KB)")

st.subheader(f"File Tree for `{workspace_root.name}`")
render_tree(workspace_root)
