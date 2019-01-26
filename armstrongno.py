x=int(input())
y=x
sum=0
while x>0:
    r=x%10
    sum=sum+r*r*r
    x=x//10
if sum==y:
    print("yes")
else:
    print("no")
