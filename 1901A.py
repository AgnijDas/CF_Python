t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    d=(x-l[-1])*2
    l.insert(0,0)
    for i in range(n):
        dif=l[i+1]-l[i]
        if dif>d:
            d=dif
    print(d)
