t=int(input())
for i in range(t):
    n=int(input())
    if n%2==1 or n<4:
        print(-1)
    else:
        max=n//4
        min=n//6 + 1 if n%6==2 or n%6==4 else n//6
        print(min,max)