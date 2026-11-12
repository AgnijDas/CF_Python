t=int(input())
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    k=[l[0]]
    g=[]
    count=1
    for i in range(1,n):
        if l[i]==l[i-1]:
            g.append(l[i])
        else:
            count+=1
            k.append(l[i])
    if len(g)>0:
        count+=1
    for i in range(1,len(g)):
        if g[i]!=g[i-1]:
            count+=1
    print(count)
    k.extend(sorted(g,reverse=True))
    print(*k)