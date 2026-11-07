import math
t=int(input())
for i in range(t):
    n=int(input())
    if n%2==0:
        print(n//2,n//2)
    else:
        a=1
        for j in range(3,int(n**0.5)+1):
            if n%j==0:
                a=n//j
                break
        print(a,n-a)