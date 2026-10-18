import gzip

VCF_PATH = "data/NA12878.chr22.GRCh38.mane.1.5.refseq.ann.vcf.gz"
vcf = gzip.open(VCF_PATH, "rt")

count = 0

snp = 0
ins = 0
delete = 0

omega = 0
alpha = 0
beta = 0
gamma = 0

omega_list = []

for line in vcf:
    if line.startswith("#"):
        continue
    count = count + 1
    fields = line.split("\t")
    ref = fields[3]
    alt = fields[4]
    info = fields[7]
    notes = info.split(";")

    for note in notes:
        if note.startswith("ANN="):
            ann = note[4:]
            annotations = ann.split(",")
            annotation = annotations[0]
            parts = annotation.split("|")
            impact = parts[2].lower()

    if impact == "high":
        omega = omega + 1
        pos = fields[1]
        gene = parts[3]
        effect = parts[1]
        gt = fields[9].split(":")[0]
        row = f"{pos:<10} {ref:<4} {alt:<4} {gene:<8} {effect:<36} {gt}"
        omega_list.append(row)
    elif impact == "moderate":
        alpha = alpha + 1
    elif impact == "low":
        beta = beta + 1
    elif impact == "modifier":
        gamma = gamma + 1

    # Note: multiallelic sites (ALT contains a comma) are not handled yet
    if len(ref) == len(alt):
        snp = snp + 1
    elif len(ref) < len(alt):
        ins = ins + 1
    else:
        delete = delete + 1

vcf.close()

print(f"Cerebro detected {count:,} mutations on chr22")
print(f"  SNPs:       {snp:>8,}   {snp / count:.1%}")
print(f"  Insertions: {ins:>8,}   {ins / count:.1%}")
print(f"  Deletions:  {delete:>8,}   {delete / count:.1%}")
print()
print(f"  Omega-level (HIGH):     {omega:>8,}   {omega / count:.1%}")
print(f"  Alpha-level (MODERATE): {alpha:>8,}   {alpha / count:.1%}")
print(f"  Beta-level (LOW):       {beta:>8,}   {beta / count:.1%}")
print(f"  Gamma-level (MODIFIER): {gamma:>8,}   {gamma / count:.1%}")
print()
print("  OMEGA-LEVEL MUTANTS")
print(f"  {'POS':<10} {'REF':<4} {'ALT':<4} {'GENE':<8} {'EFFECT':<36} GT")
for row in omega_list:
    print(f"  {row}")