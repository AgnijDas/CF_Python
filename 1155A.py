n=int(input())
l=list(input())
a=sorted(l)
if l==a:
    print("NO")
else:
    print("YES")
    for i in range(n):
        if l[i]!=a[i]:
            print(i+1,l.index(a[i],i)+1)
            break