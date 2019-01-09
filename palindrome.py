x=int(input())
sum=0
while x>0:
   r=x%10
   sum=sum*10+r
   x=x/10
if x==sum:
   print("yes")
else:
   print("no")
