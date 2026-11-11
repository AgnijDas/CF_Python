def prime(a):
    for j in range(2,int(a**0.5)+1):
        if a%j==0:
            return False
    return True
t=int(input())
for i in range(t):
    d=int(input())
    k=d+1
    while True:
        if prime(k):
            break
        k+=1
    g=k+d
    while True:
        if prime(g):
            break
        g+=1
    print(k*g)