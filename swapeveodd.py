k=input()
l=[]
for i in range(0,len(k)):
	if i%2==0:
		l.append(k[i+1])
	else:
		l.append(k[i-1])
for i in range(0,len(l)-1):
	print(l[i],end="")
print(l[-1])	
