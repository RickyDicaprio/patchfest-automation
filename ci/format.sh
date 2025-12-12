# Make this executable and then run it

#!/bin/bash

# Auto-format Python code using black
echo "=============================="
echo " Running Code Formatter (black)"
echo "=============================="

if command -v black &> /dev/null
then
    black .
else
    echo "❌ black not found. Install it using: pip install black"
    exit 1
fi

echo "✔ Formatting complete!"
