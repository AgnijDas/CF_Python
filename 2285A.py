t=int(input())
for i in range(t):
    n=int(input())
    if n<4:
        print(-1)
    else:
        l=[j for j in range(1,n+1)]
        l[0]=4
        l[3]=1
        print(*l)