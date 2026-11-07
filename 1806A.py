t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if b>d:
        print(-1)
    else:
        s=d-b
        x=a+s
        if c>x:
            print(-1)
        else:
            print(s+x-c)
