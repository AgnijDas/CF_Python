t=int(input())
for i in range (t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    if k>=2:
        print("YES")
    elif k==1:
        if l==sorted(l):
            print("YES")
        else:
            print("NO")
