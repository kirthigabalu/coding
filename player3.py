x=int(input())
rev=0
while x:
    rem=x%10
    rev=rev*10+rem
    x=x//10
print(rev)    
