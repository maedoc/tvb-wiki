#!/bin/bash
# Round 2: 2 viable models × 10 pages = 20 runs
# kimi-k2.6 and deepseek-v4-flash excluded (produce meta-commentary, not page content)

set -e

MODELS=(
    "ollama/minimax-m2.5:cloud"
    "ollama/gpt-oss:120b-cloud"
)
MODEL_NAMES=("minimax-m2.5" "gpt-oss-120b")

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

ROUND="r2"
OUTDIR="./tmp"

echo "=== Round 2 (consistency check): $(date) ==="
echo "2 models × 10 pages = 20 runs"
echo ""

DONE=0
for slug in "${SLUGS[@]}"; do
    PROMPT=$(cat "$OUTDIR/prompt_${slug}.txt")
    
    for mi in "${!MODELS[@]}"; do
        MODEL="${MODELS[$mi]}"
        MNAME="${MODEL_NAMES[$mi]}"
        OUTFILE="$OUTDIR/${ROUND}_${slug}_${MNAME}.md"
        ERRFILE="$OUTDIR/${ROUND}_${slug}_${MNAME}_err.txt"
        
        DONE=$((DONE + 1))
        echo "  [$DONE/20] $(date +%H:%M:%S) $MNAME on $slug"
        
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
echo "=== Round 2 complete: $(date) ==="
echo ""
echo "Results:"
for slug in "${SLUGS[@]}"; do
    for mi in "${!MODELS[@]}"; do
        MNAME="${MODEL_NAMES[$mi]}"
        OUTFILE="$OUTDIR/${ROUND}_${slug}_${MNAME}.md"
        if [ -s "$OUTFILE" ]; then
            WORDS=$(wc -w < "$OUTFILE")
            printf "  %-30s %-18s %4d words\n" "$slug" "$MNAME" "$WORDS"
        else
            printf "  %-30s %-18s  EMPTY\n" "$slug" "$MNAME"
        fi
    done
done