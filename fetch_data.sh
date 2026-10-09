#!/usr/bin/env bash
set -euo pipefail

SAMPLE="NA12878"
URL="https://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/release/NA12878_HG001/latest/GRCh38/HG001_GRCh38_1_22_v4.2.1_benchmark.vcf.gz"
OUT="data/${SAMPLE}.chr22.vcf.gz"

mkdir -p data

echo "Fetching $SAMPLE from Genome in a Bottle"
bcftools view -r chr22 -c 1 -O z -o "$OUT" "$URL"
bcftools index "$OUT"

echo "Done! Saved to $OUT"

