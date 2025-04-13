
# filemind/pages/assistant_scanner.py

import streamlit as st
import pandas as pd
import os
import re
from pathlib import Path

st.set_page_config(page_title="🧩 Assistant Scanner – Phase 2 Applet 8", layout="wide")
st.title("🧩 FILEMIND – Assistant Scanner")
st.markdown("Search for assistant names, codes, or known triggers inside structured or semi-structured files.")

workspace_root = Path("/mnt/data/filemind_zip_workspace/extracted")
registry_path = "/mnt/data/zip_registry.csv"
output_path = "/mnt/data/assistant_tag_map.json"

if not workspace_root.exists() or not os.path.exists(registry_path):
    st.error("Workspace or registry missing. Please run previous applets.")
    st.stop()

assistant_pattern = re.compile(r"A\d{4}|T-R-[A-Z\-]+", re.IGNORECASE)
tag_rows = []

for root, _, files in os.walk(workspace_root):
    for name in files:
        ext = name.lower().split(".")[-1]
        if ext in ["json", "csv", "md", "txt"]:
            full_path = os.path.join(root, name)
            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    matches = assistant_pattern.findall(content)
                    for match in set(matches):
                        tag_rows.append({
                            "Filename": name,
                            "Relative Path": os.path.relpath(full_path, workspace_root),
                            "Assistant Reference": match
                        })
            except Exception as e:
                st.warning(f"File skipped due to read error: {name}")

if tag_rows:
    df = pd.DataFrame(tag_rows)
    st.dataframe(df, use_container_width=True)
    df.to_json(output_path, orient="records", indent=2)
    st.success(f"✅ Assistant references saved to: {output_path}")
else:
    st.warning("No assistant patterns found.")
