#!/bin/bash

# Setam intervalul de actualizare (secunde)
INTERVAL=${INTERVAL:-5}
LOG_FILE="./system-state.log"

log_info() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') INFO: $1"
}

log_error () {
    echo "$(date '+%Y-%m-%d %H:%M:%S') ERROR: $1" >&2
}

# Citirea starii sistemului
get_system_state() {
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8"%"}')
    if [ -z "$CPU_USAGE" ]; then 
        log_error "Failed to get CPU usage"
        CPU_USAGE="N/A"
    fi

    MEM_USAGE=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')
    if [ -z "$MEM_USAGE" ]; then 
        log_error "Failed to get Memory usage"
        MEM_USAGE="N/A"
    fi

    PROC_COUNT=$(ps -e --no-headers | wc -l)
    if [ -z "$PROC_COUNT" ]; then 
        log_error "Failed to get process count"
        PROC_COUNT="N/A"
    fi

    DISK_USAGE=$(df -h / | awk 'NR==2{print $5}')
    if [ -z "$DISK_USAGE" ]; then 
        log_error "Failed to get Disk usage"
        DISK_USAGE="N/A"
    fi

    {
        echo "Timestamp: $(date)"
        echo "CPU Usage: $CPU_USAGE"
        echo "Memory Usage: $MEM_USAGE"
        echo "Active Processes: $PROC_COUNT"
        echo "Disk Usage: $DISK_USAGE"
    } > "$LOG_FILE"

    log_info "System state updated: CPU=$CPU_USAGE,MEM=$MEM_USAGE,Procs=$PROC_COUNT,Disk=$DISK_USAGE"
}

# Capturam semnale pentru oprire curata
trap "echo 'Monitor stopped'; exit 0" SIGINT SIGTERM

log_info "System monitor started, interval=${INTERVAL}s"

while true; do
    get_system_state
    sleep "$INTERVAL"
done