t=int(input())
for i in range(t):
    x,n=map(int,input().split())
    if x%2==1:
        if n%2==0:
            a=n//2
            if a%2==0:
                print(x)
            else:
                print(x-1)
        else:
            a=(n-1)//2
            if (n//2)%2==0:
                c=1
            else:
                c=-1
            if a%2==0:
                print(x+c*n)
            else:
                print(x-1+c*n)
    else:
        if n%2==0:
            a=n//2
            if a%2==0:
                print(x)
            else:
                print(x+1)
        else:
            a=(n-1)//2
            if (n//2)%2==0:
                c=-1
            else:
                c=1
            if a%2==0:
                print(x+c*n)
            else:
                print(x+1+c*n)
