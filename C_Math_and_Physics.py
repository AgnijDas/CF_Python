t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    j=1
    g=[]
    if max(l)==1:
        print(-1)
    elif len(l)-l.count(1)==1 and (max(l)==l[0] or max(l)==l[-1]):
        print(max(l))
    elif len(l)>=3 and l.count(1)+2==len(l) and l[0]!=1 and l[-1]!=1 :
        print( l[0]+l[-1]-1)
    else:
        g.append(l[0])
        while j<n-1:
            if l[j]==1:
                j=j+1
                g.append(l[j])
            else:
                g[j-1]+=1
                l[j+1]+=l[j]-1
                n=n-1
                l.pop(j)
                if j!=1:
                    j=j-1
        print(sum(l)-1)    

