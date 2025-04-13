# notion_sync_filemind.py (patched for local usage)

import os
import pandas as pd
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

notion = Client(auth=os.getenv("NOTION_API_KEY"))
db_id = os.getenv("NOTION_FILEMIND_DB_ID")

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
    local_path = os.path.join(os.getcwd(), "zip_registry.csv")
    sync_csv_to_notion(local_path, "FileMind Export")

