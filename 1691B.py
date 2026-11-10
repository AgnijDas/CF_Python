t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    g=[]
    count=1
    check=0
    for j in range(0,n-1):
        if l[j]==l[j+1]:
            count+=1
        elif count==1:
            check=1
            break
        else:
            g.extend([k for k in range(j+3-count,j+2)])
            g.append(j+2-count)
            count=1
    if check==1 or count==1:
        print(-1)
    else:
        g.extend([k for k in range(n+2-count,n+1)])
        g.append(n+1-count)
        print(*g)