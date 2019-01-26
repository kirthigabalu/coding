x,y=map(int,input().split())
l=[]
for i in range(x+1,y):
    if i%2==0:
        l.append(i)
for j in range(len(l)-1):
    print(l[j],end=" ")
print(l[-1])

