import gzip

VCF_PATH = "data/NA12878.chr22.vcf.gz"

count = 0

vcf = gzip.open(VCF_PATH, "rt")

for line in vcf:
    if line.startswith("#"):
        continue
    count = count + 1

vcf.close()

print(f"Cerebro detected {count} mutations on chr22")