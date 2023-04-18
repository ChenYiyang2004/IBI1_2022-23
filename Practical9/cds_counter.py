import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
a=re.findall(r"ATG(.+)",seq)
b=a[0].count("TAA")
c=a[0].count("TAG")
d=a[0].count("TGA")
n=b+c+d
print(n)


    