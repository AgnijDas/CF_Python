def pairs(n,l,r):
    f=0
    j=0
    k=n-1
    while j<k:
        if l[j]+l[k]<=r:
            f+=k-j
            j+=1
        else:
            k-=1
    return f
t=int(input())
for i in range(t):
    n,l,r=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    print(pairs(n,a,r)-pairs(n,a,l-1))

    