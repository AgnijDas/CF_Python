t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    gap=[]
    m=0
    k=0
    if n==2:
        gap.append(abs(l[0]-l[1]))
        k=0
        m=gap[0]
    else:
        for i in range(n-1):
            gap.append(abs(l[i]-l[i+1]))
            if gap[i]>m:
                m=gap[i]
                k=i
    if gap.count(m)>=3:
        print(m)
    elif gap.count(m)==2:
        x=gap.index(m)
        r=gap.index(m,x+1)
        a=2*max(gap[x+1:r])
        b=abs(l[x]-2*l[r])
        c=abs(l[r+1]-2*l[x+1])
        print(min(m,max(a,b,c)))
    else:
        current=m
        a=abs(l[k]-2*l[k+1])
        b=abs(2*l[k+1]-l[k+2]) if k+1!=n-1 else 0
        current=min(current,max(a,b))
        a=abs(l[k-1]-2*l[k]) if k!=0 else 0
        b=abs(2*l[k]-l[k+1])
        current=min(current,max(a,b))
        for j in range(k+2,n):
            a=abs(l[k]-2*l[j])
            b=2*max(gap[k+1:j])
            c=abs(l[k+1]-2*l[j+1]) if j!=n-1 else 0
            current=min(current,max(a,b,c))
        for j in range(k):
            a=abs(l[k+1]-2*l[j])
            b=2*max(gap[j:k]) 
            c=abs(l[k]-2*l[j-1]) if j!=0 else 0
            current=min(current,max(a,b,c))
        print(current)