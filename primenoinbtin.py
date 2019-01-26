x,y=map(int,input().split())
l=[]
for i in range(x+1,y):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.append(i)
for k in range(len(l)-1):
    print(l[k],end=" ")
print(l[-1])
