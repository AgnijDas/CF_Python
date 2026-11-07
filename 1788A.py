t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=l.count(2)
    if a%2==1:
        print(-1)
    elif a==0:
        print(1)
    else:
        c=0
        for i in range(n):
            if l[i]==2:
                c+=1
                if c==a//2:
                    break
        print(i+1)
        
