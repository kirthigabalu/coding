l=[int(x) for x in input().split()]
s=[int(x) for x in input().split()]
t=[int(x) for x in input().split()]
if l[0]==s[0] and s[0]==t[0] and t[0]==l[0]:
	print("yes")
elif l[1]==s[1] and s[1]==t[1] and t[1]==l[1]:	
	print("yes")
elif l[0]==l[1] and s[0]==s[1] and t[0]==t[1]:
	print("yes")
else:
	print("no")
