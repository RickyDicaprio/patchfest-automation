#!/usr/bin/env python3
"""
System Information Script (Python Version)
Cross-platform system information collector for automation monitoring.

This Python version provides cross-platform compatibility and can be extended
for more detailed system monitoring automation.
"""

import platform
import psutil
import argparse
import json
import sys

def get_os_info():
    """Get operating system information."""
    return {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "architecture": platform.architecture()[0],
        "machine": platform.machine(),
        "processor": platform.processor(),
        "platform": platform.platform()
    }

def get_cpu_info():
    """Get CPU information."""
    return {
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "max_frequency": f"{psutil.cpu_freq().max:.2f}MHz" if psutil.cpu_freq() else "N/A",
        "min_frequency": f"{psutil.cpu_freq().min:.2f}MHz" if psutil.cpu_freq() else "N/A",
        "current_frequency": f"{psutil.cpu_freq().current:.2f}MHz" if psutil.cpu_freq() else "N/A",
        "cpu_usage": f"{psutil.cpu_percent()}%"
    }

def get_memory_info():
    """Get memory information."""
    svmem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    return {
        "total": f"{svmem.total / (1024**3):.2f}GB",
        "available": f"{svmem.available / (1024**3):.2f}GB",
        "used": f"{svmem.used / (1024**3):.2f}GB",
        "percentage": f"{svmem.percent}%",
        "swap_total": f"{swap.total / (1024**3):.2f}GB",
        "swap_used": f"{swap.used / (1024**3):.2f}GB",
        "swap_percentage": f"{swap.percent}%"
    }

def get_disk_info():
    """Get disk usage information."""
    partitions = psutil.disk_partitions()
    disk_info = []
    
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "file_system": partition.fstype,
                "total": f"{partition_usage.total / (1024**3):.2f}GB",
                "used": f"{partition_usage.used / (1024**3):.2f}GB",
                "free": f"{partition_usage.free / (1024**3):.2f}GB",
                "percentage": f"{(partition_usage.used / partition_usage.total) * 100:.1f}%"
            })
        except PermissionError:
            # This can happen on Windows
            continue
    
    return disk_info

def print_system_info(output_format="text"):
    """Print system information in specified format."""
    
    if output_format == "json":
        # JSON output for programmatic use
        system_info = {
            "os": get_os_info(),
            "cpu": get_cpu_info(),
            "memory": get_memory_info(),
            "disk": get_disk_info()
        }
        print(json.dumps(system_info, indent=2))
        return

    # Text output for human reading
    print("=" * 50)
    print("🖥️  SYSTEM INFORMATION (Python Version)")
    print("=" * 50)
    
    # OS Information
    os_info = get_os_info()
    print(f"\n🖥️  Operating System:")
    print(f"   System: {os_info['system']}")
    print(f"   Release: {os_info['release']}")
    print(f"   Architecture: {os_info['architecture']}")
    print(f"   Machine: {os_info['machine']}")
    if os_info['processor']:
        print(f"   Processor: {os_info['processor']}")
    
    # CPU Information
    cpu_info = get_cpu_info()
    print(f"\n🔧 CPU Information:")
    print(f"   Physical Cores: {cpu_info['physical_cores']}")
    print(f"   Total Cores: {cpu_info['total_cores']}")
    print(f"   Current Usage: {cpu_info['cpu_usage']}")
    if cpu_info['max_frequency'] != "N/A":
        print(f"   Max Frequency: {cpu_info['max_frequency']}")
    
    # Memory Information
    memory_info = get_memory_info()
    print(f"\n💾 Memory Information:")
    print(f"   Total RAM: {memory_info['total']}")
    print(f"   Available RAM: {memory_info['available']}")
    print(f"   Used RAM: {memory_info['used']} ({memory_info['percentage']})")
    if float(memory_info['swap_total'].replace('GB', '')) > 0:
        print(f"   Swap Total: {memory_info['swap_total']}")
        print(f"   Swap Used: {memory_info['swap_used']} ({memory_info['swap_percentage']})")
    
    # Disk Information
    disk_info = get_disk_info()
    print(f"\n💿 Disk Usage:")
    for disk in disk_info:
        print(f"   {disk['mountpoint']} ({disk['file_system']}):")
        print(f"     Used: {disk['used']}/{disk['total']} ({disk['percentage']} full)")
        print(f"     Free: {disk['free']}")
    
    print("\n" + "=" * 50)
    print("✅ System information collected successfully!")
    print("=" * 50)

def main():
    parser = argparse.ArgumentParser(
        description="Cross-platform system information collector"
    )
    parser.add_argument(
        '--format', 
        choices=['text', 'json'],
        default='text',
        help='Output format (default: text)'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Output file (optional, defaults to stdout)'
    )
    
    args = parser.parse_args()
    
    try:
        if args.output:
            # Redirect output to file
            original_stdout = sys.stdout
            with open(args.output, 'w') as f:
                sys.stdout = f
                print_system_info(args.format)
            sys.stdout = original_stdout
            print(f"System information saved to {args.output}")
        else:
            print_system_info(args.format)
            
    except Exception as e:
        print(f"Error collecting system information: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()