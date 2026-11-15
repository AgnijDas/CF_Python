t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int, input().strip()))
    z=l.count(0)
    o=n-z
    if z>=o:
        if k>o:
            o=0
            z=n
        else:
            z+=k
            o-=k
    else:
        if k>z:
            z=0
            o=n
        else:
            z-=k
            o+=k
    print(1+z*(z+1)//2 + o*(o+1)//2)