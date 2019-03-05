#print the last n character
s,n=map(str,input().split())
N=int(n)
st="".join(reversed(s))
st1=st[:N]
string="".join(reversed(st1))
print(string)
