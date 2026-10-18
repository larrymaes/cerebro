# Cerebro 🧬

Cerebro scans a person's genetic variants and sorts them into X-Men style
"mutant power" tiers based on how much each mutation is predicted to affect
their genes.

This is a learning project for practicing bioinformatics, Python, and Git.

## How it works

1. Download one person's variants (NA12878/HG001) from NIST's public Genome in a Bottle project
2. Annotate them with SnpEff to predict what each variant does to genes
3. Cerebro reads the results and ranks each mutation:

| SnpEff impact | Mutant tier  |
|---------------|--------------|
| HIGH          | Omega-level  |
| MODERATE      | Alpha-level  |
| LOW           | Beta-level   |
| MODIFIER      | Gamma-level  |

## Status

✅ Version 1 complete.

- [x] Fetch chromosome 22 variants with bcftools
- [x] Read and count variants in Python
- [x] Classify variants as SNPs, insertions, or deletions
- [x] Annotate variants with SnpEff
- [x] Assign mutant tiers
- [x] Print a mutant report

## Requirements

- Python 3.12
- bcftools
- SnpEff

## Setup

```bash
micromamba create -n xmen -c conda-forge -c bioconda bcftools htslib snpeff python=3.12
micromamba activate xmen
```

## Usage

```bash
./fetch_data.sh      # downloads chr22 variants into data
./annotate.sh        # annotates them with SnpEff
python cerebro.py
```

Example output:

```
Cerebro detected 49,484 mutations on chr22
  SNPs:         42,625   86.1%
  Insertions:    3,537   7.1%
  Deletions:     3,322   6.7%

  Omega-level (HIGH):            3   0.0%
  Alpha-level (MODERATE):      226   0.5%
  Beta-level (LOW):            306   0.6%
  Gamma-level (MODIFIER):   48,949   98.9%

  OMEGA-LEVEL MUTANTS
  POS        REF  ALT  GENE     EFFECT                               GT
  24728176   C    T    PIWIL3   splice_donor_variant&intron_variant  0/1
  36191797   ACT  A    APOL4    frameshift_variant                   1/1
  50522253   C    T    NCAPH2   splice_donor_variant&intron_variant  0/1
```

Data files are downloaded locally and are not stored in this repo.

## Findings

- Of 49,484 variants on chromosome 22, only 3 are predicted HIGH impact (Omega-level).
- One is a 2-base deletion in APOL4 (not a whole 3-letter codon, so it shifts the reading frame), present on both copies of chr22.
- NA12878 is a healthy individual, a reminder that "high impact" means a variant likely disrupts a protein, not that it causes disease.

## Known limitations

- Multiallelic sites (480 on chr22, where ALT lists more than one allele) are not yet split, so their variant type may be misclassified.
- Only the first SnpEff annotation per variant is used, so a variant whose worst effect isn't listed first may land in a lower tier.

## Project history

Each step of the project is a separate commit. To see them:

```bash
git log --oneline
```