t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    if l.count(l[0])==n:
        if n==k:
            print("YES")
            print(*l)
        else:
            print("NO")
    elif l.count(l[-1])<=k:
        print("YES")
        print(*l[n-k:],*sorted(l[:n-k],reverse=True))
    else:
        print("NO")