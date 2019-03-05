#problem of 83
n=input()
if "/" in n:
	d=n.index("/")
	a=int(n[:d])
	b=int(n[d+1:])
	c=a//b
	print(c)
elif "%" in n:
	d=n.index("%")
	a=int(n[:d])
	b=int(n[d+1:])
	c=a%b
	print(c)
