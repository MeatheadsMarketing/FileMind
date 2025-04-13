# push_filemind_to_github.py

import os
import subprocess
from datetime import datetime

REPO_NAME = "filemind-phase2"
REPO_URL = "https://github.com/MeatheadsMarketing/FileMind.git"
BRANCH = "main"

# Setup git
print("🚀 Initializing Git repository...")
os.system("git init")
os.system(f"git remote add origin {REPO_URL}")
os.system("git branch -M main")

# Add all files
print("📁 Adding all project files...")
os.system("git add .")

# Commit with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_msg = f"FILEMIND Phase 2 Deployment - {timestamp}"
os.system(f"git commit -m \"{commit_msg}\"")

# Push
print("⬆️ Pushing to GitHub...")
os.system(f"git push -u origin {BRANCH}")

print("✅ Push complete. Your repository is live.")

