t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=l.count(max(l))
    if max(l)==min(l):
        print("NO")
    elif a==1:
        print("YES")
        print(*sorted(l,reverse=True))
    else:
        print("YES")
        l=sorted(l,reverse=True)
        for j in range(a-1):
            l.remove(max(l))
            l.append(max(l))
        print(*l)
