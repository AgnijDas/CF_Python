t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if(l!=sorted(l)):
        print(0)
        continue
    diff=l[n-1]-l[0]
    for i in range(n-1):
        if(l[i+1]-l[i] < diff):
            diff=l[i+1]-l[i]
    print(diff//2 +1)
