t=['A','k','aA','l','O','Ml','l','l0','P']
def only_upper(t):
	res=[]
	for s in t:
		if s.islower():
			res.append(s)
	return res
print(only_upper(t))
