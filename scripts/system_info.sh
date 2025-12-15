#!/bin/bash
# System Information Script
# Collects basic system information including OS, CPU, RAM, and disk usage

echo "==============================="
echo "      SYSTEM INFORMATION"
echo "==============================="

# OS Information
echo "🖥️  Operating System:"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    if command -v lsb_release &> /dev/null; then
        echo "   OS: $(lsb_release -d | cut -f2)"
        echo "   Version: $(lsb_release -r | cut -f2)"
    elif [ -f /etc/os-release ]; then
        source /etc/os-release
        echo "   OS: $PRETTY_NAME"
    else
        echo "   OS: $(uname -s) $(uname -r)"
    fi
    echo "   Architecture: $(uname -m)"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    echo "   OS: macOS $(sw_vers -productVersion)"
    echo "   Build: $(sw_vers -buildVersion)"
    echo "   Architecture: $(uname -m)"
else
    # Other Unix-like systems
    echo "   OS: $(uname -s)"
    echo "   Version: $(uname -r)"
    echo "   Architecture: $(uname -m)"
fi

echo ""

# CPU Information  
echo "🔧 CPU Information:"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux CPU info
    cpu_model=$(grep "model name" /proc/cpuinfo | head -1 | cut -d: -f2 | xargs)
    cpu_cores=$(nproc)
    echo "   Model: $cpu_model"
    echo "   Cores: $cpu_cores"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS CPU info
    cpu_model=$(sysctl -n machdep.cpu.brand_string)
    cpu_cores=$(sysctl -n hw.ncpu)
    echo "   Model: $cpu_model"
    echo "   Cores: $cpu_cores"
else
    # Fallback
    echo "   CPU: $(uname -p)"
    echo "   Cores: Available via system tools"
fi

echo ""

# Memory Information
echo "💾 Memory Information:"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux memory info
    total_mem=$(free -h | grep '^Mem:' | awk '{print $2}')
    used_mem=$(free -h | grep '^Mem:' | awk '{print $3}')
    available_mem=$(free -h | grep '^Mem:' | awk '{print $7}')
    echo "   Total RAM: $total_mem"
    echo "   Used RAM: $used_mem" 
    echo "   Available RAM: $available_mem"
    
    # Swap info
    swap_total=$(free -h | grep '^Swap:' | awk '{print $2}')
    swap_used=$(free -h | grep '^Swap:' | awk '{print $3}')
    if [ "$swap_total" != "0B" ]; then
        echo "   Swap Total: $swap_total"
        echo "   Swap Used: $swap_used"
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS memory info
    total_mem_bytes=$(sysctl -n hw.memsize)
    total_mem_gb=$((total_mem_bytes / 1024 / 1024 / 1024))
    echo "   Total RAM: ${total_mem_gb}GB"
    
    # Available memory calculation for macOS
    vm_stat_output=$(vm_stat)
    page_size=$(vm_stat | grep "page size" | awk '{print $8}')
    free_pages=$(echo "$vm_stat_output" | grep "Pages free:" | awk '{print $3}' | tr -d '.')
    available_mb=$(((free_pages * page_size) / 1024 / 1024))
    echo "   Available RAM: ${available_mb}MB"
else
    echo "   Memory information: Use system-specific tools"
fi

echo ""

# Disk Usage Information
echo "💿 Disk Usage:"
if command -v df &> /dev/null; then
    echo "   Main Partitions:"
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux - show filesystem, size, used, available, use%, mounted on
        df -h | grep -E '^/dev/' | head -5 | while read filesystem size used avail percent mountpoint; do
            echo "     $mountpoint: $used/$size ($percent full)"
        done
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS - show main disk partitions
        df -h | grep -E '^/dev/' | head -3 | while read filesystem size used avail percent mountpoint; do
            echo "     $mountpoint: $used/$size ($percent full)"
        done
    else
        # Other systems
        df -h | head -5
    fi
else
    echo "   Disk usage: df command not available"
fi

echo ""

# Additional System Information
echo "ℹ️  Additional Info:"
echo "   Hostname: $(hostname)"
echo "   Current User: $(whoami)"
echo "   Shell: $SHELL"
echo "   Current Directory: $(pwd)"

# Uptime
if command -v uptime &> /dev/null; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "   Uptime: $(uptime | awk '{print $3, $4}' | tr -d ',')"
    else
        echo "   Uptime: $(uptime -p 2>/dev/null || uptime)"
    fi
fi

echo ""
echo "==============================="
echo "✅ System information collected successfully!"
echo "==============================="
