t=int(input())
import math
for i in range(t):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    m=sum([math.ceil(j/x) for j in l])
    print(math.ceil(sum(l)/x),m)