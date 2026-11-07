t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    count=1
    m=1
    for j in range(n-1):
        if l[j]==l[j+1]:
            count+=1
        elif count>m:
            m=count
            count=1
        else:
            count=1
    if count>m:
        m=count
    if m==n:
        print(0)
    else:
        opp=0
        while True:
            opp+=1
            if 2*m >= n:
                opp+=n-m
                print(opp)
                break
            else:
                opp+=m
                m=m*2