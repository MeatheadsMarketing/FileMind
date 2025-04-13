
# filemind/pages/file_registry_table.py

import streamlit as st
import pandas as pd
import os
from pathlib import Path

st.set_page_config(page_title="📑 File Registry Table – Phase 2 Applet 3", layout="wide")
st.title("📑 FILEMIND – File Registry Table")
st.markdown("Analyze and interact with file metadata from extracted ZIP.")

workspace_root = Path("/mnt/data/filemind_zip_workspace/extracted")

if not workspace_root.exists():
    st.warning("❌ No files found. Please run ZIP Loader and Directory Visualizer first.")
    st.stop()

file_data = []
for root, _, files in os.walk(workspace_root):
    for name in files:
        full_path = Path(root) / name
        rel_path = full_path.relative_to(workspace_root)
        file_data.append({
            "Filename": name,
            "Relative Path": str(rel_path),
            "Extension": full_path.suffix.lower(),
            "Size (KB)": round(full_path.stat().st_size / 1024, 2),
            "Last Modified": pd.to_datetime(full_path.stat().st_mtime, unit='s')
        })

df = pd.DataFrame(file_data)
st.dataframe(df, use_container_width=True)

output_path = "/mnt/data/zip_registry.csv"
df.to_csv(output_path, index=False)
st.success(f"✅ File registry saved: {output_path}")
