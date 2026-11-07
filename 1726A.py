t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if n==1:
        print(0)
        continue
    d=0 
    for i in range(n-1):
        if l[i]-l[i+1]>d:
            d=l[i]-l[i+1]
    if l[-1]-l[0]>d:
        d=l[-1]-l[0]
    d2=max(l[1:])-l[0]
    d3=l[-1]-min(l[:n-1])
    print(max(d,d2,d3))