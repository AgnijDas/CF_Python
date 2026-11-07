t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if (a+c)%(2*b)==0:
        print("YES")
    elif a<2*b and (2*b-a)%c==0:
        print("YES")
    elif 2*b>c and (2*b-c)%a==0:
        print("YES")
    else:
        print("NO")