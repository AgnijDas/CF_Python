t=int(input())
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l=[2**i for i in l]
    l.sort(reverse=True)
    b=h=0
    for i in l:
        if b<=h:
            b+=i
        else:
            h+=i
    print(b*h)
    