k,b=map(int,input().split())
count=0
for i in range(k,b+1):
	for j in range(2,i+1):
		if i%j==0:
			break
	if i==j:
		count=count+1
print(count)	
