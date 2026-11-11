t=int(input())
for i in range(t):
    w,h=map(int,input().split())
    l=list(map(int,input().split()))
    b1=l[-1]-l[1]
    l=list(map(int,input().split()))
    b2=l[-1]-l[1]
    l=list(map(int,input().split()))
    b3=l[-1]-l[1]
    l=list(map(int,input().split()))
    b4=l[-1]-l[1]
    a1=max(b1,b2)*h
    a2=max(b3,b4)*w
    print(max(a1,a2))

    