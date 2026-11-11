t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    d={}
    for x in l:
        d[x]=d.get(x,0)+1
    g=[]
    uniq=sorted(d.keys(),reverse=True)
    for j in range(len(uniq)):
        qty=d[uniq[j]]
        if qty==0:
            continue
        if j==len(uniq)-1:
            g.extend([uniq[-1]]*qty)
            break
        g.extend([uniq[j]]*qty)
        for k in range(j+1,len(uniq)):
            if d[uniq[k]]==0:
                continue
            elif d[uniq[k]]<=qty:
                g.extend([uniq[k]]*d[uniq[k]])
                d[uniq[k]]=0
            else:
                g.extend([uniq[k]]*qty)
                d[uniq[k]]-=qty
    print(*g)
        
