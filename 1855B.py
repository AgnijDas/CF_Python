t=int(input())
for i in range(t):
    n=int(input())
    for j in range(1,51):
        if n%j!=0:
            print(j-1)
            break

