# 🧠 FILEMIND Phase 2 – Modular Streamlit Applet System

This directory contains all Phase 2 applets for FILEMIND: a modular AI-powered file intelligence system.

---

## 🔧 Contents

- 20 fully functional Streamlit tabs (one per applet step)
- Master dashboard control panel: `filemind_dashboard.py`
- Registry-powered: reads and updates `zip_registry.csv`
- ZIP lifecycle from upload to metadata audit and export bundle

---

## 📋 Applet Summary

| Applet ID | Script | Function |
|-----------|--------|----------|
| 1 | `zip_loader.py` | Upload and extract `.zip` |
| 2 | `directory_visualizer.py` | Tree view of extracted contents |
| 3 | `file_registry_table.py` | Build and view file registry |
| 4 | `size_tagger.py` | Classify files by size |
| 5 | `gpt_export_identifier.py` | Detect ChatGPT export patterns |
| 6 | `extension_summary_chart.py` | Filetype pie chart |
| 7 | `shortcut_scanner.py` | Extract `#SHORTCUTS` from text |
| 8 | `assistant_scanner.py` | Tag assistant references |
| 9 | `manual_tag_editor.py` | Manually assign tags |
| 10 | `auto_categorizer.py` | GPT-driven role classification |
| 11 | `file_viewer_previewer.py` | Readable file previews |
| 12 | `scan_formatter.py` | Prepare scanable markdown |
| 13 | `output_router.py` | Route files to Scan, Export, Merge |
| 14 | `summary_table_generator.py` | Generate content summaries |
| 15 | `confidence_scorer.py` | Rank file usefulness |
| 16 | `cluster_sorter.py` | Group files by purpose |
| 17 | `final_output_table.py` | Unified view of all file states |
| 18 | `bundle_zipper.py` | Create a ZIP from selected files |
| 19 | `audit_summary_viewer.py` | View audit logs |
| 20 | `save_bundle_output.py` | Final master ZIP of results |

---

## 🚀 How to Launch

1. Ensure Python + Streamlit are installed
2. Run from CLI:

```bash
streamlit run filemind_dashboard.py
```

3. Navigate to any applet from the dashboard or Streamlit sidebar

---

## 📁 Data Folder Structure

- `/mnt/data/zip_registry.csv`: master file metadata
- `/mnt/data/filemind_zip_workspace/`: extracted zip contents
- `/mnt/data/file_summaries.csv`, `zip_filemap.csv`, etc.: per-app outputs
