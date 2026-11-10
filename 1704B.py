t=int(input())
for j in range(t):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    m1=l[0]
    m2=l[0]
    c=0
    for i in range(1,n):
        if l[i]>m1:
            m1=l[i]
        elif l[i]<m2:
            m2=l[i]
        if (m1-m2)> 2*x:
            c+=1
            m1=l[i]
            m2=l[i]
    print(c)

    