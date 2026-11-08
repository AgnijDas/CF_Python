t=int(input())
for i in range(t):
    n,k,q=map(int,input().split())
    l=list(map(int,input().split()))
    days=0
    count=0
    for j in range(n):
        if l[j]<=q:
            count+=1
        else:
            if count>=k:
                k1=k
                while k1<=count:
                    days+=count-k1+1
                    k1+=1
            count=0
    if count>=k:
        while k<=count:
            days+=count-k+1
            k+=1
    print(days)