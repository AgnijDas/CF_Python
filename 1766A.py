t=int(input())
for i in range(t):
    n=int(input())
    for i in range(1,7):
        if n<10**i:
            print(9*(i-1) + n//(10**(i-1)))
            break
