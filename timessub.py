l=[int(a) for a in input().split()]
m=[int(b) for b in input().split()]
hr=l[0]-m[0]
minutes=l[1]-m[1]
print(abs(hr),abs(minutes))
