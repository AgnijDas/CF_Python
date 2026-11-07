t=int(input())
for k in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if l==sorted(l):
        print("YES")
    else:
        check=0
        for i in range(1,n-1):
            for j in range(1,n-i):
                if l[j]>l[j-1] and l[j]>l[j+1]:
                    l[j],l[j+1]=l[j+1],l[j]
        if(l==sorted(l)):
            print("YES")
        else:
            print("NO")
            
