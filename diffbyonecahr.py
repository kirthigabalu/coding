k,l=map(str,input().split())
count=0
for i in range(0,len(k)):
	if k[i]!=l[i]:
		count=count+1
if count>1:
	print("no")
else:
	print("yes")
