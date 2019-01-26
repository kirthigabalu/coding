x=int(input())
l=[]
for i in range(1,6):
    p=x*i
    l.append(p)
for j in range(len(l)-1):
    print(l[j],end=" ")
print(l[-1])

