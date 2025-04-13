
# filemind/pages/scan_formatter.py

import streamlit as st
import pandas as pd
import os
from pathlib import Path
import shutil

st.set_page_config(page_title="🧹 Scan Formatter – Phase 2 Applet 12", layout="wide")
st.title("🧹 FILEMIND – Scan Prep Formatter")
st.markdown("Format files marked for scan and convert them to `.md` if needed.")

workspace_root = Path("/mnt/data/filemind_zip_workspace/extracted")
scan_ready_dir = Path("/mnt/data/filemind_scan_ready")
scan_ready_dir.mkdir(exist_ok=True, parents=True)
registry_path = "/mnt/data/zip_registry.csv"

if not os.path.exists(registry_path):
    st.error("File registry not found. Run File Registry Table first.")
    st.stop()

df = pd.read_csv(registry_path)

if "Categorized Intent" in df.columns:
    candidates = df[df["Categorized Intent"].str.contains("scan", case=False, na=False)]
else:
    candidates = df[df["Extension"].isin([".txt", ".md"])]

if not candidates.empty:
    st.markdown("### ✅ Files marked for scan:")
    st.dataframe(candidates[["Filename", "Relative Path"]], use_container_width=True)

    if st.button("Convert Files for Scan"):
        copied = 0
        for _, row in candidates.iterrows():
            src = workspace_root / row["Relative Path"]
            dest = scan_ready_dir / (row["Filename"].replace(".txt", ".md"))
            shutil.copyfile(src, dest)
            copied += 1
        st.success(f"Copied and formatted {copied} files to scan-ready folder.")
        st.info(f"Output folder: `{scan_ready_dir}`")
else:
    st.warning("⚠️ No files found marked for scan.")
