t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    m=0
    r=0
    check=0
    for i in range(0,n):
        if l.count(i)+r >=k and l.count(i)>=1:
            m=m+1
            r=r+l.count(i)-k
        else:
            print(m)
            check=1
            break
    if check==0:
        print(m)
    
