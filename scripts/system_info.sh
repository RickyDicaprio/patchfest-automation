#!/bin/bash
# System Information Script

echo "==============================="
echo "      SYSTEM INFORMATION"
echo "==============================="

echo "Hostname: $(hostname)"
echo "User: $(whoami)"
echo "Current Directory: $(pwd)"
echo "OS: $(uname -o)"
echo "Kernel: $(uname -r)"
echo "Uptime: $(uptime -p)"
echo "Memory Usage:"
free -h

echo "==============================="
echo "Script executed successfully!"
