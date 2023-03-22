#total number is 2 and generations is 1 at the beginning
total_number=2
generations=1
#While the total number of rabbits is no more than 100
while total_number<=100:
	#variable"born number" is the number of rabbits that will be born each generation
	born_number=2**generations
	#	total number plus born number of this generation
	total_number=total_number+born_number
	#	generations plus one
	generations=generations+1
#print the generations
a="Over 100 rabbits have been born untill "
b=str(generations)
c="th generation"
print(a+b+c)

