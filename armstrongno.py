x,y=map(int,input().split())
l=[]
for i in range(x+1,y):
    p=i
    sum=0
    while i>0:
        r=i%10
        sum=sum+r*r*r
        i=i//10
    if sum==p:
        l.append(p)
for j in range(len(l)-1):
    print(l[j],end=" ")
print(l[-1])

