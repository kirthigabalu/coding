#finding whether the no is present or not
N,k=map(int,input().split())
l=[int(a) for a in input().split()]
c=0
for i in range(0,len(l)):
	if l[i]==k:
		c=c+1
if c>0:
	print("yes")
else:
	print("no")
