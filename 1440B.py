import math
t=int(input())
for j in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=0
    index=math.ceil(n/2)+1 if n%2==0 else math.ceil(n/2)
    m=index
    for i in range(k):
        s+=l[-m]
        m+=index
    print(s)

