yr=int(input())
if (yr%4==0 and yr%100==0) or yr%400==0:
    print("yes")
else:
    print("no")
