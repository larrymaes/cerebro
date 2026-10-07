# Cerebro 🧬

Cerebro scans a person's genetic variants and sorts them into X-Men style
"mutant power" tiers based on how much each mutation is predicted to affect
their genes.

This is a learning project for practicing bioinformatics, Python, and Git.

## How it works

1. Download one person's variants from the public 1000 Genomes Project
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

## Requirements

- Python 3.12
- bcftools
- SnpEff

## Usage

Coming soon!