t=int(input())
for k in range(t):
    n=int(input())
    l=list(input())
    count=0
    ans=0
    d={}
    for i in range(n):
        if d.get(l[i],0)==0:
            d[l[i]]=1
            count+=1
        ans+=count
    print(ans)