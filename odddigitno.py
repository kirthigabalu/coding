#odd number digit will be displayed
x=int(input())
l=[]
while x:
	rem=x%10
	if rem%2==1:
		l.append(rem)
	x=x//10
l.reverse()
for i in range(0,len(l)-1):
	print(l[i],end=" ")
print(l[-1])
