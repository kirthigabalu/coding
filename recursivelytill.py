#printing recursively
n=int(input())
if n%2==0:
	while n%2==0:
		a=n//2
		n=n//2
else:
	print(n)
print(a)	
