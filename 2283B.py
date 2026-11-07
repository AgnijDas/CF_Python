t=int(input())
for k in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    m=0
    for i in range(n):
        count=0
        for j in range(n):
            if l[j]%l[i]==0:
                count+=1
        if count>m:
            m=count
    print(n-m)
            