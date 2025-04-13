
# filemind_dashboard.py

import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

st.set_page_config(page_title="🧠 FILEMIND Dashboard", layout="wide")
st.title("🧠 FILEMIND – Phase 2 Dashboard")
st.caption("Central control hub for ZIP intelligence applets")

st.markdown("### 🔍 System Summary")
col1, col2, col3, col4 = st.columns(4)

try:
    df = pd.read_csv("/mnt/data/zip_registry.csv")
    col1.metric("📁 Files Loaded", len(df))
    col2.metric("📦 Routed Files", df["Routing"].notna().sum())
    col3.metric("🏷️ Tagged Files", df["Manual Tags"].notna().sum())
    col4.metric("🧬 Clusters", df["Cluster Group"].nunique())
except:
    col1.error("No registry")
    col2.empty()
    col3.empty()
    col4.empty()

st.markdown("---")
st.markdown("### 🚀 Quick Access Panel")
apps = [
    "zip_loader.py", "directory_visualizer.py", "file_registry_table.py", "size_tagger.py",
    "gpt_export_identifier.py", "extension_summary_chart.py", "shortcut_scanner.py", "assistant_scanner.py",
    "manual_tag_editor.py", "auto_categorizer.py", "file_viewer_previewer.py", "scan_formatter.py",
    "output_router.py", "summary_table_generator.py", "confidence_scorer.py", "cluster_sorter.py",
    "final_output_table.py", "bundle_zipper.py", "audit_summary_viewer.py", "save_bundle_output.py"
]

for app in apps:
    st.markdown(f"- [{app.replace('.py','').replace('_',' ').title()}](./{app})")

st.markdown("---")
st.markdown("### 📑 Registry Preview")
if os.path.exists("/mnt/data/zip_registry.csv"):
    st.dataframe(pd.read_csv("/mnt/data/zip_registry.csv"), use_container_width=True)
else:
    st.info("zip_registry.csv not found. Upload and process ZIP archive to begin.")
