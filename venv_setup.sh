#!/bin/bash

# venv_setup.sh
# Creates and activates virtual environment for FILEMIND + installs dependencies

echo "🛠️ Creating Python virtual environment in .venv..."
python3 -m venv .venv

if [ -d ".venv" ]; then
  echo "✅ Virtual environment created."
  echo "🔁 Activating .venv..."
  source .venv/bin/activate
  echo "📦 Installing required packages: pandas, notion-client, python-dotenv..."
  pip install --upgrade pip
  pip install pandas notion-client python-dotenv
  echo "✅ Packages installed. Freezing requirements..."
  pip freeze > requirements.txt
  echo "📄 requirements.txt updated."
  echo "🧠 Virtual environment ready. Run: source .venv/bin/activate"
else
  echo "❌ Failed to create virtual environment. Check Python installation."
fi

