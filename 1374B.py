t=int(input())
for i in range(t):
    n=int(input())
    a=b=n
    c=d=0
    while a>=2:
        if a%2==0:
            c+=1
            a=a//2
        else:
            break
    while b>=3:
        if b%3==0:
            d+=1
            b=b//3
        else:
            break
    if ((2**c) * (3**d)) != n or d<c:
        print(-1)
    else:
        print(2*d-c)
