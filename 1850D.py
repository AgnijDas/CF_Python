t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    a=[]
    c=1
    for j in range(n):
        if j==n-1:
            a.append(c)
            break
        if l[j+1]-l[j]<=k:
            c+=1
        else:
            a.append(c)
            c=1
    print(n-max(a))
