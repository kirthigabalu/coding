n,k=map(int,input().split())
N=[int(x) for x in input().split()]
k=[int(x) for x in input().split()]
l=[]
for i in range(0,len(k)):
	N.append(k[i])
	a=max(N)
	l.append(a)
for i in range(0,len(l)-1):
	print(l[i],end=" ")
print(l[-1])	
