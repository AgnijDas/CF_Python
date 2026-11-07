t = int(input())

for _ in range(t):
    n = int(input())

    if n % 4 == 0:
        x = n
    elif n % 4 == 1:
        x = 1
    elif n % 4 == 2:
        x = n + 1
    else:
        x = 0

    p = n.bit_length() - 1

    s = [0] * (p + 1)
    s[p] = 1

    for j in range(p, 0, -1):
        s[j-1] = 1 ^ ((x >> j) & 1) ^ s[j]

    d = [0] * n

    for j in range(p + 1):
        if s[j]:
            d[(1 << j) - 1] = 1

    print(*d)