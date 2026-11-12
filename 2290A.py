t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if c-b==1 and b-a==1:
        print("YES")
    else:
        print("NO")

    