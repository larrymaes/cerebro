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

🚧 Work in progress

- [x] Fetch chromosome 22 variants with bcftools
- [x] Read and count variants in Python
- [x] Classify variants as SNPs, insertions, or deletions
- [x] Annotate variants with SnpEff
- [ ] Assign mutant tiers
- [ ] Print a mutant report

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
./fetch_data.sh      # downloads chr22 variants into data/
./annotate.sh        # annotates them with SnpEff
python cerebro.py
```

Example output:

```
Cerebro detected 49,484 mutations on chr22
  SNPs:         42,625   86.1%
  Insertions:    3,537   7.1%
  Deletions:     3,322   6.7%
```

Data files are downloaded locally and are not stored in this repo.

## Known limitations

- Multiallelic sites (480 on chr22, where ALT lists more than one allele) are not yet split, so their variant type may be misclassified.

## Project history

Each step of the project is a separate commit. To see them:

```bash
git log --oneline
```
