#!/usr/bin/env bash

# Get the directory of the current script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Use the script directory to locate the requirements.txt
python3 -m pip install -r "$SCRIPT_DIR/requirements.txt"