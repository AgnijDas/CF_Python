t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    if k==4:
        check=0
        count=0
        for j in range(n):
            if l[j]%4==0:
                check=2
                print(0)
                break
            elif l[j]%2==0:
                count+=1
                if count==2:
                    print(0)
                    check=2
                    break
            elif l[j]%4==3:
                check=1
        if check==1:
            print(1)
        elif check==0:
            print(min(2-count,2))
    else:
        check=0
        a=0
        for j in range(n):
            if l[j]%k==0:
                check=1
                print(0)
                break
            elif l[j]%k>a:
                a=l[j]%k
        if check==0:
            print(k-a)