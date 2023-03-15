#variable"born number" is the number of rabbits that will be born each generation
#total number is 2 and generations is 1 at the beginning
#While the total number of rabbits is no more than 100
#	total number plus born number of this generation
#	generations plus one
#print the generations

total_number=2
generations=1
while total_number<=100:
	born_number=2**generations
	total_number=total_number+born_number
	generations=generations+1
a="Over 100 rabbits have been born untill "
b=str(generations)
c="th generation"
print(a+b+c)

