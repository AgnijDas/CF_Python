t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l=list(set(l))
    n=len(l)
    l.sort()
    g=[l[0]]
    for i in range(1,n):
        g.append(l[i]-l[i-1])
    start1=0
    idx=0
    while idx<n-1:
        if g[idx]==1:
            start1+=1
            idx+=1
        else:
            break
    if start1%2==0:
        print("Alice")
    else:
        print("Bob")