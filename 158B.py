import math
n=int(input())
l=list(map(int,input().split()))
a=l.count(1)
b=l.count(2)
c=l.count(3)
d=l.count(4)
if c>=a:
    print(a+abs(c-a)+d+b//2+b%2)
else:
    e=a-c
    count=c+d+b//2
    if b%2==1:
        count+=1
        if e>=2:
            count+=math.ceil((e-2)/4)
    else:
        count+=math.ceil(e/4)
    print(count)
