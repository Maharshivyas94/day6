l=[2,3,4,234,[123,23,760],12,[45,8],9,10]
def nested_sum(l):
	total=0
	for i in  l:
		if isinstance(i,list):
			total+=nested_sum(i)
		else:
			total+=i
	return total
print(nested_sum(l)) 

