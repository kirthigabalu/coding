
x=int(input())
l=[int(a) for a in input().split()]
m=sorted(l)
for i in range(0,len(m)-1):
  print(m[i],end=" ")
print(m[-1])

