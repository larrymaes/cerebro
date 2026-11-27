#!/usr/bin/env bash
set -euo pipefail

#Sources the unified config file.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/config.sh"

IN="${SCRIPT_DIR}/data/${SAMPLE}.${REGION}.vcf.gz"
OUT="${SCRIPT_DIR}/data/${SAMPLE}.${REGION}.${GENOME}.ann.vcf.gz"
STATS="${SCRIPT_DIR}/data/${SAMPLE}.${REGION}.${GENOME}.snpEff_summary.html"

echo "Annotating $SAMPLE with SnpEff ($GENOME)..."
snpEff -Xmx8g -stats "$STATS" "$GENOME" "$IN" | bgzip > "$OUT"
bcftools index "$OUT"

echo "Done! Saved to $OUT"