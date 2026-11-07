t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    c=n-a-b
    if c>=2:
        print("YES")
    elif c==0 or c==1 :
        print("NO")
    elif a==n and b==n:
        print("YES")
    else:
        print("NO")
