k=input()
l=[]
for i in range(0,len(k)):
	if k[i].islower():
		n=k[i].upper()
		l.append(n)
	else:
		n=k[i].lower()
		l.append(n)
s1="".join(l)		
print(s1)
