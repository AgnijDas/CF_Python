t=int(input())
for i in range(t):
    n=int(input())
    if n%2==1:
        print("YES")
    else:
        check=0
        while n>=2:
            if n%2==1:
                check=1
                break
            else:
                n=n//2
        if check==1:
            print("YES")
        else:
            print("NO")