#!/bin/bash

# git_sync_forcefix.sh
# Quickly commits and pushes all updates while enforcing FILEMIND policies

echo "🧠 Running placeholder audit..."
BAD_FILES=$(grep -rl 'placeholder' pages/ | wc -l)

if [ "$BAD_FILES" -gt 0 ]; then
  echo "❌ Found placeholder content in pages/. Fix before pushing."
  grep -rl 'placeholder' pages/
  exit 1
else
  echo "✅ No placeholder files detected. Proceeding with commit."
fi

# Stage changes
git add .
git commit -m "🔁 Sync + push all FILEMIND updates [forcefix clean]"
git push

echo "✅ Push complete. GitHub now synced with fixed deploy."

