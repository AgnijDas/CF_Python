t=int(input())
for i in range(t):
    n,k,x=map(int,input().split())
    if x>k*(2*n - k + 1)//2 or x<k*(k+1)//2:
        print("NO")
    elif k*(k+1)//2 == x:
        print("YES")
    else:
        a=x-k*(k+1)//2
        check=0
        for j in range(k):
            b=n-(2*j+1)
            if b>a:
                if b+j+1>k:
                    print("YES")
                    check=1
                    break
                else:
                    print("NO")
                    check=1
                    break
            else:
                a=a-b
                if a==0:
                    print("YES")
                    check=1
                    break
        if check==0:
            print("NO")
        

