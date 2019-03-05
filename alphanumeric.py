#alphanumeric and print it
s=input()
l=list(s)
for i in range(0,len(l)):
	if l[i].isnumeric():
		print(l[i],end="")
