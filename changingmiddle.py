#changing the middle element include*
n=int(input())
c=0
for i in range(2,n-1):
    if n%i==0:
       c=c+1
    else:
       continue
if c==0:
    print("no")
else:
    print("yes")
