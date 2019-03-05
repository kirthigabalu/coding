#first finding the diff and check it is odd or even
n,k=map(int,input().split())
s=abs(n-k)
if s%2==0:
	print("even")
else:
	print("odd")
