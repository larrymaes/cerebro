import gzip

VCF_PATH = "data/NA12878.chr22.vcf.gz"

count = 0
SNP = 0
ins = 0
delete = 0

vcf = gzip.open(VCF_PATH, "rt")

for line in vcf:
    if line.startswith("#"):
        continue
    count = count + 1
    fields = line.split("\t")
    ref = fields[3]
    alt = fields[4]
    if len(ref) == len(alt):
        SNP = SNP + 1
    elif len(ref) < len(alt):
        ins = ins + 1
    else:
        delete = delete + 1

vcf.close()

print(f"Cerebro detected {count:,} mutations on chr22")
print(f"  SNPs:       {SNP:>8,}   {SNP / count:.1%}")
print(f"  Insertions: {ins:>8,}   {ins / count:.1%}")
print(f"  Deletions:  {delete:>8,}   {delete / count:.1%}")