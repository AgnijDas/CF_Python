t=int(input())
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    avg=sum(l)/n
    index=0
    diff=abs(l[0]-avg)
    for i in range(1,n):
        if abs(l[i]-avg)<diff :
            diff=abs(l[i]-avg)
            index=i
    cost=sum(l)-l[i]*l.count(l[i])
    opp=l[-1]-l[i] + l[i]-l[0]
    print(cost, opp)