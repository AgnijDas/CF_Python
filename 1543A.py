import math
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a==b:
        print(0,0)
    else:
        c=abs(a-b)
        if a%c==b%c:
            print(c,min(a%c,c-(a%c)))
        else:
            print(c,min(a,b))