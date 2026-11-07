t=int(input())
for i in range (t):
    n=int(input())
    l=list(map(int,input().split()))
    if max(l)!=min(l):
        a=l.count(max(l))
        print(len(l)-a,a)
        print(*sorted(l)[0:len(l)-a])
        print(*([max(l)]*a))
    else:
        print(-1)
