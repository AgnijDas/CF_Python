t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    if sum(l)==n:
        print(-1)
    elif sum(l)==n-2+l[0]+l[-1]:
        print(l[0]+l[-1]-1)
    else:
        print(sum(l)-1)