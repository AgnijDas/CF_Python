t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if l.count(n)==3:
        print(0)
    else:
        print(max([(n-i) for i in l]))