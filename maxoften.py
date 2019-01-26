l=[int(a) for a in input().split()]
maxi=0
for i in range(0,len(l)):
    if maxi<l[i]:
        maxi=l[i]
print(maxi)
