#!/bin/bash
echo "🚀 PatchFest Automation Environment Ready!"
echo "Available scripts in /app/scripts/:"
ls -la scripts/
echo ""
echo "Usage examples:"
echo "  python scripts/sample_hello.py"
echo "  python scripts/backup_folder.py --help"
echo "  python scripts/cleanup_temp.py --help"
echo ""

# If arguments provided, run them
if [ $# -gt 0 ]; then
    echo "Running: $@"
    exec "$@"
else
    # Default: run sample hello script
    echo "Running default script..."
    python scripts/sample_hello.py
fi
