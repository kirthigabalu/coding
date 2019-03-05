b,k=map(int,input().split())
l=[]
for i in range(1,11):
	if b%i==0 and k%i==0:
		l.append(i)
print(max(l))		
