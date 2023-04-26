import blosum
import re
blosum=blosum.BLOSUM(62)

def exact_seq(filename):
	'''
	input the fasta file
	return the amino acid sequence
	'''
	a=open(filename,"r")
	seq=""
	for line in a:
		if re.search(r"^>.+",line)== None:
			b = line.replace("\n", "")
			seq +=b
	return seq
		

def calculate(seq1,seq2,pairname):
	'''
	input the two sequence to compare
	print BLOSUM score and identity percentage
	'''
	score=0
	edit_distance=0 #set	initial	distance	as	zero
	for	i	in	range(len(seq1)): #compare	each	amino	acid
		score += blosum[seq1[i]][seq2[i]]
		if	seq1[i]!=seq2[i]:		
			edit_distance	+=	1 
	a=len(seq1)-edit_distance
	percentage=a/len(seq1)*100	
	print(pairname)
	print("seq1:"+seq1+"\n"+"seq2:"+seq2)
	print("final BLOSUM score:"+str(score))
	print("the percentage identity:"+ str(percentage)+"%"+"\n")
#use the function to calculate BLOSUM score and identity percentage	
human=exact_seq("ACE2_human.fa")
mouse=exact_seq("ACE2_mouse.fa")
cat=exact_seq("ACE2_cat.fa")
calculate(human,mouse,"human-mouse")
calculate(mouse,cat,"mouse-cat")
calculate(human,cat,"human-cat")
