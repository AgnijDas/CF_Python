import math
t=int(input())
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    b=[]
    for i in range(n):
        a=abs(l[i]-i-1)
        if a!=0 :
            b.append(a)
    g=0
    for i in b:
        g=math.gcd(g,i)
    print(g)
