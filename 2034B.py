t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    s=input()
    count=0
    ans=0
    i=0
    while i<n:
        if s[i]=='0':
            count+=1
        else:
            count=0
        if count==m:
            ans+=1
            count=0
            i+=k
        else:
            i+=1
    print(ans)
