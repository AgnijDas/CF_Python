t= int(input())
for i in range(t):
    n,m=map(int,input().split())
    p=list(input())
    q=list(input())
    check=0
    for j in q:
        if j in p:
            p.remove(j)
        else:
            check=1
            break
    if check==1:
        print("NO")
    else:
        if ["i","s","x"]==sorted(p):
            print("YES")
        else:
            print("NO")
