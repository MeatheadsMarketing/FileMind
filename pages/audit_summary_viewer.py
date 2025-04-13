
# filemind/pages/audit_summary_viewer.py

import streamlit as st
import os

st.set_page_config(page_title="📋 Audit Summary Viewer – Phase 2 Applet 19", layout="wide")
st.title("📋 FILEMIND – Audit Summary Viewer")
st.markdown("Display summary findings from your Phase 2 filemap and zip contents.")

summary_path = "/mnt/data/zip_audit_report.md"

if os.path.exists(summary_path):
    with open(summary_path, "r") as f:
        st.markdown(f.read())
    st.success("✅ Audit summary loaded.")
else:
    st.warning("⚠️ No audit summary found. Please run prior audits or zip builders to generate one.")
