
# filemind/pages/bundle_zipper.py

import streamlit as st
import zipfile
import os
from pathlib import Path

st.set_page_config(page_title="📦 Bundle Zipper – Phase 2 Applet 18", layout="wide")
st.title("📦 FILEMIND – Bundle Zipper")
st.markdown("Package tagged and routed files into deployable bundles.")

workspace_dir = Path("/mnt/data/filemind_zip_workspace/extracted")
registry_path = "/mnt/data/zip_registry.csv"

if not os.path.exists(registry_path):
    st.error("Missing zip_registry.csv. Please complete prior phases.")
    st.stop()

import pandas as pd
df = pd.read_csv(registry_path)

cluster_types = df["Cluster Group"].dropna().unique().tolist()
selected_cluster = st.selectbox("Select cluster group to bundle", cluster_types)

zip_name = st.text_input("Output ZIP filename", value="bundle_export.zip")
export_path = Path(f"/mnt/data/{zip_name}")

if st.button("📦 Build ZIP Bundle"):
    with zipfile.ZipFile(export_path, 'w') as zipf:
        subset = df[df["Cluster Group"] == selected_cluster]
        for _, row in subset.iterrows():
            full_path = workspace_dir / row["Relative Path"]
            if full_path.exists():
                arcname = f"{selected_cluster}/{row['Filename']}"
                zipf.write(full_path, arcname=arcname)
    st.success(f"✅ Bundle created: {export_path}")
    st.markdown(f"[Download ZIP](sandbox:{export_path})")
