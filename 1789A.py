import math
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if 1 in l or 2 in l:
        print("YES")
    else:
        check=0
        for j in range(n):
            for k in range(j+1,n):
                a=math.gcd(l[j],l[k])
                if a==1 or a==2:
                    check=1
                    break
                    
            if check==1:
                print("YES")
                break
        if check==0:
            print("NO")
