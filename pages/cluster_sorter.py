
# filemind/pages/cluster_sorter.py

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="🧬 Cluster Sorter – Phase 2 Applet 16", layout="wide")
st.title("🧬 FILEMIND – Intelligence Cluster Sorter")
st.markdown("Group files into thematic clusters for downstream batch logic.")

registry_path = "/mnt/data/zip_registry.csv"

if not os.path.exists(registry_path):
    st.error("zip_registry.csv not found. Please run prior registry builders.")
    st.stop()

df = pd.read_csv(registry_path)
cluster_tags = ["Scan Bundle", "Merge Assets", "Assistant Docs", "Reference", "Discard"]

selected_files = st.multiselect("Select files to assign to a cluster", df["Filename"].tolist())
cluster_label = st.selectbox("Choose cluster label", cluster_tags)

if "Cluster Group" not in df.columns:
    df["Cluster Group"] = ""

if selected_files and st.button("Assign Cluster"):
    df.loc[df["Filename"].isin(selected_files), "Cluster Group"] = cluster_label
    df.to_csv(registry_path, index=False)
    st.success(f"✅ Assigned {len(selected_files)} files to cluster: {cluster_label}")
    st.dataframe(df[df["Filename"].isin(selected_files)], use_container_width=True)
else:
    st.info("Choose files and a label to assign.")
