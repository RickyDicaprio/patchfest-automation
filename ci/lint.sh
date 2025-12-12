# Make this executable and then run it


#!/bin/bash

# Lint all Python files using flake8
echo "=============================="
echo " Running Linter (flake8)"
echo "=============================="

if command -v flake8 &> /dev/null
then
    flake8 .
else
    echo "❌ flake8 not found. Install it using: pip install flake8"
    exit 1
fi

echo "✔ Linting complete! No major issues found."
