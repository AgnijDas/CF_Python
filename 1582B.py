t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=l.count(0)
    b=l.count(1)
    print((b)*(2**a))