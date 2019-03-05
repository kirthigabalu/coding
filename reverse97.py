#printing the reverse 
x=int(input())
r=0
while x:
    rem=x%10
    r=r*10+rem
    x=x//10
print(r)    
