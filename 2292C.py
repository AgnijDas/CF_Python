t=int(input())
for i in range(t):
    n=int(input())
    l=list(input())
    l=[int(j) for j in l]
    if n%2==1:
        print("NO")
    else:
        check=0
        for i in range(1,n):
            if l[i]==l[i-1]:
                check=1
                break
        if check==1:
            print("YES")
        else:
            print("NO")
    