t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=d=0
    for j in a:
        if j%2==0:
            c+=1
    for j in b:
        if j%2==0:
            d+=1
    if k%2==1:
        if c>=d:
            print("YES")
        else:
            print("NO")
    else:
        if (n-c)>=(n-d):
            print("YES")
        else:
            print("NO")