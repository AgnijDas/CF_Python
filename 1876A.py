t=int(input())
for i in range(t):
    n,p=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if p<=min(b):
        print(n*p)
    elif n==1:
        print(p)
    else:
        c=[]
        for j in range(n):
            c.append([b[j],a[j]])
        c.sort()
        rem=n-1
        cost=p
        for i in range(n):
            if c[i][0]<p:
                if rem>c[i][1]:
                    rem-=c[i][1]
                    cost+=c[i][0]*c[i][1]
                else:
                    cost+=c[i][0]*rem
                    rem=0
                    break
        print(cost+rem*p)