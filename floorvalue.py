#finding the floor value
l=[int(i) for i in input().split()]
for i in range(0,len(l)):
	if 100 in l:
		l.remove(100)
if len(l)==1:
	print(l[0])
else:
	print(l[0]*l[1])
