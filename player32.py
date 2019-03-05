#kiki
n,k=map(int,input().split())
c=0
l=[int(x) for x in input().split()]
for i in range(0,len(l)):
	if l[i]==k:
		c=c+1
if c>0:
	print("Yes")
else:
	print("No")
