n=int(input())
l=list(input())
a=sorted(l[:n])
b=sorted(l[n:])
check=0
if a[0]>b[0]:
    for j in range(1,n):
        if a[j]<=b[j]:
            check=1
            print("NO")
            break
    if check==0:
        print("YES")
elif a[0]<b[0]:
    for j in range(1,n):
        if a[j]>=b[j]:
            check=1
            print("NO")
            break
    if check==0:
        print("YES")
else:
    print("NO")