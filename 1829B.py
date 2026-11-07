t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    m=0
    c=0
    for i in l:
        if i==0:
            c+=1
        else:
            if c>m:
                m=c
            c=0
    if(c>m):
        m=c
    print(m)
