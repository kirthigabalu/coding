#checkimg the perfect square
import math
n,m=map(int,input().split())
M=n*m
i=int(math.sqrt(M))
if M==i*i:
    print("yes")
else:
    print("no")
