t=int(input())
for i in range(t):
    n=int(input())
    s=list(input())
    m=1
    c=0
    for j in range(n-1):
        if s[j]==s[j+1]:
            m+=1
        else:
            if m>c:
                c=m
            m=1
    if m>c:
        c=m
    print(c+1)