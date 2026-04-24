#!/bin/bash
# Complete remaining R1 runs: free-energy-principle, mean-field-theory, stochastic-differential-equations
set -e

MODELS=(
    "ollama/kimi-k2.6:cloud"
    "ollama/minimax-m2.5:cloud"
    "ollama/gpt-oss:120b-cloud"
    "ollama/deepseek-v4-flash:cloud"
)
MODEL_NAMES=("kimi-k2.6" "minimax-m2.5" "gpt-oss-120b" "deepseek-v4-flash")

SLUGS=(
    "free-energy-principle"
    "mean-field-theory"
    "stochastic-differential-equations"
)

echo "=== Resuming R1: $(date) ==="

for slug in "${SLUGS[@]}"; do
    PROMPT=$(cat "./tmp/prompt_${slug}.txt")
    
    for mi in "${!MODELS[@]}"; do
        MODEL="${MODELS[$mi]}"
        MNAME="${MODEL_NAMES[$mi]}"
        OUTFILE="./tmp/r1_${slug}_${MNAME}.md"
        ERRFILE="./tmp/r1_${slug}_${MNAME}_err.txt"
        
        if [ -s "$OUTFILE" ]; then
            WORDS=$(wc -w < "$OUTFILE")
            if [ "$WORDS" -gt 50 ] && ! grep -q "404 - Page Not Found" "$OUTFILE" 2>/dev/null; then
                echo "  SKIP $MNAME $slug ($WORDS words)"
                continue
            fi
        fi
        
        echo "  $(date +%H:%M:%S) $MNAME on $slug"
        pi --no-sandbox --model "$MODEL" -p "$PROMPT" > "$OUTFILE" 2> "$ERRFILE"
        
        if [ -s "$OUTFILE" ]; then
            if grep -q "404 - Page Not Found" "$OUTFILE" 2>/dev/null; then
                echo "    -> ERROR: 404"
                echo "" > "$OUTFILE"
            else
                WORDS=$(wc -w < "$OUTFILE")
                echo "    -> $WORDS words"
            fi
        else
            echo "    -> EMPTY"
        fi
    done
done

echo ""
echo "=== R1 complete: $(date) ==="