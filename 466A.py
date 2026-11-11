n,m,a,b=map(int,input().split())
c=0
if b/m>=a:
    print(n*a)
else:
    c=0
    while n-m>=0:
        c+=b
        n=n-m
    print(c+min(n*a,b))

    