#!/bin/bash
SLUGS="antspy arbor bids-validator bidscoin brainstorm brian brian2 coreneuron dipy dynasim eeglab fieldtrip freesurfer fsl fsleyes mne-python mrtrix mrtrix3 netpyne neuroml nilearn nwb pynn simnibs spm tvb-adapters tvb-library"
OUTDIR="tmp/bulk_rewrite"
MODEL="ollama/minimax-m2.5:cloud"
LOG="tmp/entity_rewrite.log"

echo "=== Entity rewrite started ===" > "$LOG"
date >> "$LOG"

SUCCESS=0
FAIL=0
for slug in $SLUGS; do
    echo "[$(date +%H:%M:%S)] Rewriting $slug..." >> "$LOG"
    python3 scripts/bulk_rewrite.py --slug "$slug" --model "$MODEL" --outdir "$OUTDIR" --no-commit 2>> "$LOG"
    if [ $? -eq 0 ]; then
        SUCCESS=$((SUCCESS+1))
        echo "  ✓ $slug OK" >> "$LOG"
    else
        FAIL=$((FAIL+1))
        echo "  ✗ $slug FAILED" >> "$LOG"
    fi
    sleep 2
done

echo "=== Results: $SUCCESS passed, $FAIL failed ===" >> "$LOG"
date >> "$LOG"
