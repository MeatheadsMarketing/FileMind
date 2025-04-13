#!/bin/bash

# git_stage_filemind_restore.sh
# Force stages only real deploy logic from your current FILEMIND folder

echo "🧠 Staging real FILEMIND deploy files..."

FILES=(
  filemind_dashboard.py
  requirements.txt
  .streamlit_config.toml
)

for FILE in "${FILES[@]}"; do
  if [[ -f "$FILE" ]]; then
    git add "$FILE"
    echo "✅ Staged: $FILE"
  else
    echo "⚠️ Missing: $FILE (not staged)"
  fi
done

# Add all applet .py files if present
count=$(ls *.py 2>/dev/null | grep -v "filemind_dashboard.py" | wc -l)
if [[ $count -gt 0 ]]; then
  git add *.py
  echo "✅ Applet files staged ($count total)"
else
  echo "⚠️ No applet .py files found."
fi

# Commit & push
git commit -m "🔁 Restore full logic – FILEMIND Phase 2 Deployment"
git push

echo "✅ Push complete. GitHub is now synced."

