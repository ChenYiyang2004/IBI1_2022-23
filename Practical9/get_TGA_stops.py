import re
import os
os.chdir("./")
a=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
b=open("TGA_genes.fa","w")
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
	if re.search(r".+TGA$",d[i]):
		b.write(d[i])
a.close()
b.close()			

	