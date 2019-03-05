#checking the number
n=int(input())
l,u=map(int,input().split())
count=0
for i in range(l+1,u):
	if n==i:
		count=count+1
if count>0:
	print("yes")
else:
	print("no")
