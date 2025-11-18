#!/bin/bash
# Simple launcher script for INR-USD Currency Converter

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3 to run this application."
    exit 1
fi

# Run the application
python3 currency_converter.py
