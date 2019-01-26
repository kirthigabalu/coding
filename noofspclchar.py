n=input()
c=0
for i in range(0,len(n)):
    if n[i]>="a" and n[i]<="z" or n[i]>="A" and n[i]<="Z":
        c=c
    elif n[i].isnumeric():
        c=c
    else:
        c=c+1
print(c)
