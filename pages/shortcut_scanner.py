
# filemind/pages/shortcut_scanner.py

import streamlit as st
import pandas as pd
import os
from pathlib import Path
import re

st.set_page_config(page_title="🏷️ Shortcut Scanner – Phase 2 Applet 7", layout="wide")
st.title("🏷️ FILEMIND – Shortcut Scanner")
st.markdown("Scan for embedded shortcuts like `#S1`, `#X`, `#EXPORT-MD-FULL` in readable text files.")

workspace_root = Path("/mnt/data/filemind_zip_workspace/extracted")
registry_path = "/mnt/data/zip_registry.csv"
output_path = "/mnt/data/zip_shortcut_index.csv"

if not workspace_root.exists() or not os.path.exists(registry_path):
    st.error("ZIP or file registry not found. Run earlier applets first.")
    st.stop()

shortcut_pattern = re.compile(r"#\w+[\-\w]*")
index_rows = []

for root, _, files in os.walk(workspace_root):
    for name in files:
        ext = name.lower().split(".")[-1]
        if ext in ["txt", "md", "csv"]:
            full_path = os.path.join(root, name)
            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                matches = shortcut_pattern.findall(content)
                if matches:
                    for shortcut in set(matches):
                        index_rows.append({
                            "Filename": name,
                            "Relative Path": os.path.relpath(full_path, workspace_root),
                            "Shortcut Detected": shortcut
                        })

if index_rows:
    df_shortcuts = pd.DataFrame(index_rows)
    st.dataframe(df_shortcuts, use_container_width=True)
    df_shortcuts.to_csv(output_path, index=False)
    st.success(f"✅ Detected and saved to: {output_path}")
else:
    st.warning("No shortcuts found.")
