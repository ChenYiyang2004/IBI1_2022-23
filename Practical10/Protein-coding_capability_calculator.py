import re
def distance (seq):
	"""
	Input: a DNA sequence
	return the percentage of this sequence which is	coding and whether the sequence should be labelled as ‘protein-coding’,	‘non-coding’, or ‘unclear’
	"""
	a=seq.upper()
	b=re.findall(r"ATG.+TGA",a)
	percent=len(b[0])/len(a)*100
	c=str(percent)+"%"
	if percent>50:
		d="protein-coding"
	elif percent<10:
		d="non-coding"
	else:
		d="unclear"	
	output="Percentage:"+c+"\n"+"This sequence should be labelled as\t"+d	
	return output
#example			
print(distance("GggggatggTGA"))	