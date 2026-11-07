t=int(input())
for j in range(t):
    n,k,x=map(int,input().split())
    if x!=1:
        print("YES")
        if x!=k:
            print(n//k + n%k)
            print((str(k)+" ")*(n//k)+"1 "*(n%k))
        else:
            print(n//(k-1) + n%(k-1))
            print((str(k-1)+" ")*(n//(k-1))+"1 "*(n%(k-1)))
    else:
        if(k==1):
            print("NO")
        elif((n%k)%2==0):
            print("YES")
            print(n//k + (n%k)//2)
            print((str(k)+" ")*(n//k)+"2 "*((n%k)//2))
        elif n%k!=1:
            print("YES")
            print(n//k + 1)
            print((str(k)+" ")*(n//k)+str(n%k)+" ")
        else:
            check=0
            for i in range(k,1,-1):
                for m in range((n//i),0,-1):
                    if((n-i*m)%2==0):
                        check=1
                        print("YES")
                        print(m + (n-i*m)//2)
                        print((str(i)+" ")*(m)+"2 "*((n-i*m)//2))
                        break
                if(check==1):
                    break     
            if check==0:
                print("NO")
                    
