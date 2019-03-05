k=int(input())
sum=0
while k>0:
	r=k%10
	sq=r*r
	sum=sum+sq
	k=k//10
print(sum)
