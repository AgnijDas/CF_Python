d,s = map(int, input().split())
MIN=list()
MAX=list()
for i in range(d):
    a,b=map(int, input().split())
    MIN.append(a)
    MAX.append(b)
if(s>sum(MAX) or s<sum(MIN)):
    print("NO")
else:
    balance=s-sum(MIN)
    sch=MIN.copy()
    for i in range(d):
        balance-=MAX[i]-MIN[i]
        sch[i]=MAX[i]
        if balance==0:
            print("YES")
            for i in sch:
                print(i,end=" ")
            break
        elif balance<0:
            sch[i]=sch[i]+balance
            print("YES")
            for i in sch:
                print(i,end=" ")
            break
    if(balance>0):
        print("NO")
    
