t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=l.count(1)
    b=l.count(-1)
    if a>=b :
        if b%2==0:
            print(0)
        else:
            print(1)
    else:
        d=b-a
        opp=d//2 + d%2
        b=b-opp
        if b%2==0:
            print(opp)
        else:
            print(opp+1)
