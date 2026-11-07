t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    c = []
    for i in range(n-1):
        c.append(b[i])
        if b[i] > b[i+1]:
            c.append(b[i+1])
    c.append(b[-1])
    print(len(c))
    print(*c)
