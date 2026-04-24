#!/bin/bash
# Round 1: 4 models × 10 pages = 40 runs
set -e

MODELS=(
    "ollama/kimi-k2.6:cloud"
    "ollama/minimax-m2.5:cloud"
    "ollama/gpt-oss:120b-cloud"
    "ollama/deepseek-v4-flash:cloud"
)

MODEL_NAMES=("kimi-k2.6" "minimax-m2.5" "gpt-oss-120b" "deepseek-v4-flash")

SLUGS=(
    "epileptor"
    "dynamic-causal-modeling"
    "fokker-planck-equation"
    "bifurcation-theory"
    "tractography"
    "hopfield"
    "variational-bayes"
    "free-energy-principle"
    "mean-field-theory"
    "stochastic-differential-equations"
)

ROUND="${1:-r1}"
OUTDIR="./tmp"

echo "=== Round $ROUND: $(date) ==="
echo "4 models × 10 pages = 40 runs"
echo ""

TOTAL=0
DONE=0
for slug in "${SLUGS[@]}"; do
    PROMPT_FILE="$OUTDIR/prompt_${slug}.txt"
    PROMPT=$(cat "$PROMPT_FILE")
    
    for mi in "${!MODELS[@]}"; do
        MODEL="${MODELS[$mi]}"
        MNAME="${MODEL_NAMES[$mi]}"
        OUTFILE="$OUTDIR/${ROUND}_${slug}_${MNAME}.md"
        ERRFILE="$OUTDIR/${ROUND}_${slug}_${MNAME}_err.txt"
        
        TOTAL=$((TOTAL + 1))
        
        if [ -s "$OUTFILE" ]; then
            WORDS=$(wc -w < "$OUTFILE")
            # Skip if file has substantial content (not just error HTML)
            if [ "$WORDS" -gt 50 ] && ! grep -q "404 - Page Not Found" "$OUTFILE" 2>/dev/null; then
                echo "  SKIP $ROUND $MNAME $slug ($WORDS words, already exists)"
                DONE=$((DONE + 1))
                continue
            fi
        fi
        
        echo "  [$DONE/$TOTAL] $ROUND $MNAME on $slug ($(date +%H:%M:%S))"
        
        pi --no-sandbox --model "$MODEL" -p "$PROMPT" > "$OUTFILE" 2> "$ERRFILE"
        
        if [ -s "$OUTFILE" ]; then
            # Check for HTML error pages
            if grep -q "404 - Page Not Found" "$OUTFILE" 2>/dev/null; then
                echo "    -> ERROR: 404 response"
                echo "" > "$OUTFILE"
            else
                WORDS=$(wc -w < "$OUTFILE")
                echo "    -> $WORDS words"
            fi
        else
            echo "    -> EMPTY"
        fi
        
        DONE=$((DONE + 1))
    done
done

echo ""
echo "=== Round $ROUND complete: $(date) ==="
echo ""
echo "Results summary:"
for slug in "${SLUGS[@]}"; do
    for mi in "${!MODELS[@]}"; do
        MNAME="${MODEL_NAMES[$mi]}"
        OUTFILE="$OUTDIR/${ROUND}_${slug}_${MNAME}.md"
        if [ -s "$OUTFILE" ]; then
            WORDS=$(wc -w < "$OUTFILE")
            printf "  %-25s %-18s %4d words\n" "$slug" "$MNAME" "$WORDS"
        else
            printf "  %-25s %-18s  EMPTY\n" "$slug" "$MNAME"
        fi
    done
done