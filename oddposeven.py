#printing odd position seperately and even position separetly
s=input()
l=list(s)
l1=[]
l2=[]
for i in range(0,len(l)):
	if i%2==0:
		l1.append(l[i])
	else:
		l2.append(l[i])
print("".join(l1),"".join(l2))
