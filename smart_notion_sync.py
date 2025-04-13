# smart_notion_sync.py
# Locates zip_registry.csv anywhere under FileMind and syncs to Notion

import os
import pandas as pd
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

notion = Client(auth=os.getenv("NOTION_API_KEY"))
db_id = os.getenv("NOTION_FILEMIND_DB_ID")


def find_csv(target="zip_registry.csv"):
    for root, _, files in os.walk(os.getcwd()):
        if target in files:
            return os.path.join(root, target)
    return None


def sync_csv_to_notion(file_path, title_prefix):
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        notion.pages.create(
            parent={"database_id": db_id},
            properties={
                "Name": {"title": [{"text": {"content": f"{title_prefix} – {row.get('Filename', 'Untitled')}"}}]},
                "Extension": {"rich_text": [{"text": {"content": str(row.get('Extension', ''))}}]},
                "Routing": {"select": {"name": str(row.get('Routing', 'None'))}},
                "Tags": {"multi_select": [{"name": tag.strip()} for tag in str(row.get('Manual Tags', '')).split(',') if tag]}
            }
        )


if __name__ == "__main__":
    path = find_csv("zip_registry.csv")
    if path:
        print(f"✅ Found: {path}")
        sync_csv_to_notion(path, "FileMind Export")
    else:
        print("❌ zip_registry.csv not found. Run File Registry Table in Streamlit first.")

