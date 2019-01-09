x=int(input())
y=x
k=0
while x>0:
    r=x%10
    k=k+r*r*r
    x=x//10
if k==y:
    print("yes")
else:
    print("no")
