t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    mex=[]
    for j in range(n):
        g=l[:j+1]
        for m in range(n+1):
            if m not in g:
                mex.append([m,j])
                break
    mex.sort(reverse=True)
    idx=mex[k-1][1]
    if mex[k-1][0]==idx+1:
        print(-1)
    else:
        print(l.index(max(l[0:idx+1]))+1,l.index(mex[k-1][0])+1)