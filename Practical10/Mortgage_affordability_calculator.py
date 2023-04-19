def house (v,s):
	"""
	Input: v,value of a house. s, annual salary of purchaser
	Returns  "Yes" if the purchaser can buy the house, otherwise "No"
	"""
	if 5*s>=v:
		return "Yes"
	else:
		return "No"

#example
a=house(180000,35000)
print(a)