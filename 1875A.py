t=int(input())
for i in range(t):
    a,b,n=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    t=b-1
    for i in l:
        if i>=a:
            t+=a-1
        else:
            t+=i
    print(t+1)
