k,b=map(str,input().split())
cout=0
if len(k)!=len(b):
	print("no")
else:
	for i in range(0,len(k)):
		n=k.count(k[i])
		m=b.count(b[i])
		if n==m:
			cout=0
		else:
			cout=cout+1
	if cout==0:
		print("yes")
	else:
		print("no")
