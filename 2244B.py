t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    rem=0
    check=0
    for j in range(n):
        if l[j]+rem<j+1:
            check=1
            break
        else:
            rem+=l[j]-(j+1)
    print("NO") if check==1 else print("YES")
