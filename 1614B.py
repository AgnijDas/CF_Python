t=int(input())
for m in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    g=[]
    for j in range(n):
        g.append([l[j],j])
    g.sort(reverse=True)
    k=[0]*(n+1)
    a=1
    count=0
    ans=0
    for i in range(n):
        if count==2:
            a+=1
            count=0
        ans+=2*g[i][0]*a
        k[g[i][1]+1]=a*(-1)**count
        count+=1
    print(ans)
    print(*k)