s=input()
l=list(s)
b="."
l.append(b)
for i in range(0,len(l)-1):
	print(l[i],end="")
print(l[-1])	
