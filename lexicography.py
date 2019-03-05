#finding lexicography
n=input()
l=list(n)
l1=sorted(l)
for i in range(0,len(l1)-1):
	print(l1[i],end="")
print(l1[-1])	
