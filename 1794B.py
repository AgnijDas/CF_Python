t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    g=[]
    if l[0]==1:
        g.append(2)
    else:
        g.append(l[0])
    for j in range(1,n):
        if l[j]==1:
            if g[j-1]==2:
                g.append(3)
            else:
                g.append(2)
        elif l[j]%g[j-1]==0:
            g.append(l[j]+1)
        else:
            g.append(l[j])
    print(*g)