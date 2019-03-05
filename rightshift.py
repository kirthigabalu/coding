k,b=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,b):
	count=l[-1]
	a=l.remove(l[-1])
	l.insert(0,count)
for i in range(0,len(l)-1):
	print(l[i],end=" ")
print(l[-1])	
