import math
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a==b:
        print(0)
    elif a%2==1 and b%2==1:
        print(-1)
    else:
        m1=max(a,b)
        m2=min(a,b)
        if m1%m2!=0:
            print(-1)
        else:
            c=m1//m2
            if c&(c-1):
                print(-1)
            else:
                c=c.bit_length()-1
                print(c//3 + (c%3)//2 + (c%3)%2)
            

