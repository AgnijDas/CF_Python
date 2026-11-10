t=int(input())
for j in range(t):
    n,k=map(int,input().split())
    l=list(input())
    m=0
    c=0
    for i in range(n):
        if i<=k-1:
            if l[i]=="B":
                c+=1
                m+=1
        else:
            if l[i]=="W" and l[i-k]=="B":
                c-=1
            elif l[i]=="B" and l[i-k]=="W":
                c+=1
                if c>m:
                    m=c
    print(k-m)
    