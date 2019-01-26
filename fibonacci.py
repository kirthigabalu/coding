n=int(input())
l=[]
i=1
frst=0
sec=1
while i<=n:
    if i<=1:
        next=i
    else:
        next=frst+sec
        frst=sec
        sec=next
    l.append(next)
    i=i+1
for j in range(len(l)-1):
    print(l[j],end=" ")
print(l[-1])
