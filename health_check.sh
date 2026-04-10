#!/bin/bash

echo "===== System Health Check ====="

echo ""

echo "--- Disk Space ---"
df -h

echo ""
echo "--- Memory Usage ---"
free -h

echo ""
echo "--- Top 5 Running Processes ---"
ps aux --sort=-%cpu | head -6

echo ""
echo "===== Check Complete ====="

