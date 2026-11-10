t=int(input())
for i in range(t):
    n,k,b,s=map(int,input().split())
    if s>= k*b and s<= b*k + n*(k-1):
        if n==1:
            print(s)
        else:
            rem=s-k*b
            l=[]
            l.append(k*b)
            for j in range(0,n):
                if rem<=(k-1):
                    if j==0:
                        l[0]+=rem
                    else:
                        l.append(rem)
                    break
                else:
                    if j==0:
                        l[0]+=k-1
                    else:
                        l.append(k-1)
                    rem-=(k-1)
            l.extend([0]*(n-len(l)))
            print(*l)
    else:
        print(-1)