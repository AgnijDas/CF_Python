t=int(input())
for i in range(t):
    n=int(input())
    for j in range(n):
        z=int(input())
        l=sorted(list(map(int,input().split())))
        if j==0:
            ans=l[1]
            a1=l[1]
            a2=l[0]
        else:
            ans+=l[1]
            if l[0]<a2:
                a2=l[0]
            if l[1]<a1:
                a1=l[1]
    print(ans-a1+a2)
            
        

