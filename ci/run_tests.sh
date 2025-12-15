# Make this executable and then run it


#!/bin/bash

# Run all Python tests
echo "=============================="
echo " Running Python Tests"
echo "=============================="

if command -v pytest &> /dev/null
then
    pytest -q
else
    echo "❌ pytest not found. Install it using: pip install pytest"
    exit 1
fi

echo "✔ Tests completed successfully!"

