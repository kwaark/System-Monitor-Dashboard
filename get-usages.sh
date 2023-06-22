#!/bin/bash
echo "$(date '+%d-%m-%Y %H:%M')"
echo -n "MEM. RAM - Total: "
free -m | awk 'NR==2 {printf "%sMB", $2}'
echo -n " Used: "
free -m | awk 'NR==2 {printf "%sMB\n", $3}'
echo -n "CPU% - Used: "
mpstat | awk 'NR==4 {usage = 100 - $NF; printf "%.2f%%\n", usage}'