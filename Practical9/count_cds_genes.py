import re
import os
input=input("input	one	of	the	three stop	codons (TAA’,‘TAG’ or ‘TGA’)")
filename=input+"_stop_genes.fa"
os.chdir("./")
a=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
b=open(filename,"w")
d=[]
c=0
for line in a:
	if line.startswith('>'):
		d.append(c)
		name=line.split()[0]
		c=name+"\n"
	else:
		line=line.replace("\n","")		
		c=c+line
del d[0]
for i in range(0,len(d)):
	if re.search(f".+{input}$",d[i]):
		seq=d[i]
		number=seq.count(f"{input}")
		y=re.search(r"(^>.+)(\n.+)",seq)
		h=y.group(1)+"\t"+str(number)+y.group(2)+"\n"
		b.write(h)
a.close()
b.close()			
	





       