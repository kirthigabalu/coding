#find the product
n=int(input())
pro=1
while n:
    rem=n%10
    pro=pro*rem
    n=n//10
print(pro)    
