#print the index of the changed number
x=int(input())
ls=[int(x) for x in input().split()]
for i in range(1,len(ls)):
    if ls[i-1]>ls[i]:
        print(i-1)
