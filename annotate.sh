#!/usr/bin/env bash
set -euo pipefail

SAMPLE="NA12878"
GENOME="GRCh38.mane.1.5.refseq"
IN="data/${SAMPLE}.chr22.vcf.gz"
OUT="data/${SAMPLE}.chr22.${GENOME}.ann.vcf.gz"
STATS="data/${SAMPLE}.chr22.${GENOME}.snpEff_summary.html"

echo "Annotating $SAMPLE with SnpEff ($GENOME)..."
snpEff -Xmx8g -stats "$STATS" "$GENOME" "$IN" | bgzip > "$OUT"
bcftools index "$OUT"

echo "Done! Saved to $OUT"