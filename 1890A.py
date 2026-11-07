t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if n==2:
        print("YES")
        continue
    l.sort()
    a=l[0]
    c=[]
    c.append(l.count(a))
    for j in l:
        if j!=a:
            a=j
            c.append(l.count(a))
    if len(c)>2:
        print("NO")
    elif len(c)==1:
        print("YES")
    elif len(c)==2 and (abs(c[0]-c[1])==1 or abs(c[0]-c[1])==0) :
        print("YES")
    else:
        print("NO")
    
