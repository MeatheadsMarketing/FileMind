
# filemind/pages/thread_parser_viewer_plugin.py

import streamlit as st
import os
import json

st.set_page_config(page_title="📜 ThreadParser Plugin – FILEMIND Add-on", layout="wide")
st.title("📜 FILEMIND – ThreadParser Viewer Plugin")
st.caption("Modular plugin to inspect full markdown thread exports and sync with Notion or GitHub.")

index_path = "/mnt/data/thread_index.json"
if os.path.exists(index_path):
    with open(index_path, "r") as f:
        threads = json.load(f)
    options = [t.get("thread_name", f"Thread {i+1}") for i, t in enumerate(threads)]
    selected = st.selectbox("Select a thread to view", options)
    st.success(f"Selected: {selected}")
else:
    st.warning("No thread index available.")

st.markdown("### 📖 Markdown Thread Export")
md_path = "/mnt/data/thread_FULL_EXPORT_REBUILT.md"
if os.path.exists(md_path):
    with open(md_path, "r") as f:
        content = f.read()
        st.code(content[:3000], language="markdown")
else:
    st.warning("Thread markdown not found.")
