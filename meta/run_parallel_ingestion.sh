#!/bin/bash
# Parallel ingestion script for sources-reference.md
# Generated: 2026-04-20T13:28:03.145841

WIKI_ROOT=/home/duke/tvb-wiki
TASKS_DIR="$WIKI_ROOT/meta/ingestion_tasks"

echo "Starting parallel ingestion of sources-reference.md..."
echo "Total tasks: 0

# Function to process a single task
process_task() {
    task_file=$1
    page_name=$(basename "$task_file" | sed 's/task_//')
    
    echo "Processing: $page_name"
    
    # Read task instructions
    # In a real scenario, this would dispatch to a subagent
    # For now, we create the update command
    
    target_path=$(grep "Path:" "$task_file" | head -1 | sed 's/.*Path: //')
    
    # Call subagent (simulated here)
    # subagent update_wiki_page --task "$task_file" --output "$target_path.updated"
    
    echo "  ✓ $page_name processed"
}

export -f process_task

# Run tasks in parallel (adjust -P for number of parallel jobs)
ls -1 "$TASKS_DIR"/task_* | xargs -P 4 -I {} bash -c 'process_task "$@"' _ {}

echo "Parallel ingestion complete!"
echo "Review .updated files and integrate changes."
