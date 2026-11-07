t=int(input())
for j in range(t):
    n,q=map(int,input().split())
    z=list(map(int,input().split()))
    prefix=[0]*(n+1)
    for i in range(0,n):
        prefix[i+1]=prefix[i]+z[i]
    for i in range(q):
        l,r,k=map(int,input().split())
        s=prefix[n]-(prefix[r]-prefix[l-1])+(r-l+1)*k
        if s%2==1:
            print("YES")
        else:
            print("NO")