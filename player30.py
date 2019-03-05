p,r,m=map(str,input().split())
N=int(m)
count=0
if len(p)!=len(r):
	pritn("no")
else:
	for i in range(0,len(p)):
		if p[i]!=r[i]:
			count=count+1
if count==N:
	print("yes")
else:
	print("no")
