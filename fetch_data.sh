#!/usr/bin/env bash
set -euo pipefail

#Sources the unified config file.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/config.sh"
OUT="${SCRIPT_DIR}/data/${SAMPLE}.${REGION}.vcf.gz"

mkdir -p "${SCRIPT_DIR}/data"

#Different datasets use differing nomenclature for chromosomes, so this will automate the prefix.
CONTIGS=$(bcftools index -s "$URL" | cut -f1)
QUERY_REGION="$REGION"
if ! echo "$CONTIGS" | grep -qx "$QUERY_REGION"; then
    if [[ "$QUERY_REGION" == chr* ]] && echo "$CONTIGS" | grep -qx "${QUERY_REGION#chr}"; then
        QUERY_REGION="${QUERY_REGION#chr}"
    elif [[ "$QUERY_REGION" != chr* ]] && echo "$CONTIGS" | grep -qx "chr${QUERY_REGION}"; then
        QUERY_REGION="chr${QUERY_REGION}"
    fi
fi

echo "Fetching $SAMPLE from Genome in a Bottle"
bcftools view -r "$QUERY_REGION" -c 1 -O z -o "$OUT" "$URL"
bcftools index "$OUT"

echo "Done! Saved to $OUT"

