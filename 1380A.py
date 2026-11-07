t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if l==sorted(l) or l==sorted(l,reverse=True):
        print("NO")
    else:
        j=-1
        for m in range(1,n-1):
            i=k=-1
            for p in range(m):
                if l[m]>l[p]:
                    i=p
                    break
            if i==-1:
                continue
            else:
                for p in range(m+1,n):
                    if l[m]>l[p]:
                        k=p
                        break
            if k!=-1:
                j=m
                break
        if j!=-1:
            print("YES")
            print(i+1,j+1,k+1)
        else:
            print("NO")
