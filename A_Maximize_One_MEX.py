t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    mex=[]
    for j in range(n):
        check=0
        for m in range(0,j+1):
            a=l[0:j+1]
            if m not in a:
                mex.append(m)
                check=1
                break
        if check==0:
            mex.append(j+1)
    c=mex.index(sorted(mex,reverse=True)[k-1])
    if (c+1)==n:
        print(-1)
    else:
        check=0
        for m in range(mex.count(mex[c])):
            for j in range(0,c+1):
                a=sorted(l[0:c+1])
                if j!=a[j]:
                    print(l.index(max(a))+1,l.index(j)+1)
                    check=1
                    break
            if check==1:
                break
            else:
                c=c+1



