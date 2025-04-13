# 📜 ThreadParser Viewer Plugin – FILEMIND Integration

This plugin module allows full markdown thread previewing and simulated sync options (GitHub + Notion) inside the FILEMIND ecosystem.

---

## 🧠 What It Does

- Loads a list of thread exports from `thread_index.json`
- Displays markdown file (typically `thread_FULL_EXPORT_REBUILT.md`) in a scrollable preview
- Triggers stub actions for:
  - `notion_sync_threadparser.py`
  - `push_threadparser_github.py`
- Integrates visually with FILEMIND's navigation + dashboard

---

## 🔧 File Dependencies

- `thread_index.json` – JSON list of thread names or IDs
- `thread_FULL_EXPORT_REBUILT.md` – Markdown thread content
- `.env` (optional) – Environment file for Notion/GitHub keys

---

## ✅ Installation

Drop `thread_parser_viewer_plugin.py` into your `pages/` folder inside the Streamlit FILEMIND app.

Launch via:

```bash
streamlit run filemind_dashboard.py
```

---

## 🔁 Output

No files are written. This is a **read + trigger plugin**.
