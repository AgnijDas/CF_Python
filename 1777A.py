t=int(input())
for j in range (t):
    n=int(input())
    l=list(map(int,input().split()))
    l=[i%2 for i in l]
    c=0
    i=0
    while i<n-1:
        if l[i]==l[i+1]:
            l.remove(l[i])
            n=n-1
            c=c+1
        else:
            i=i+1
    print(c)
    
