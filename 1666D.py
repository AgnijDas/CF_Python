n=int(input())
for _ in range(n):
    s,t=map(str,input().split())
    s=list(s)
    t=list(t)
    k=[]
    check=1
    for i in s:
        if i in t:
            a=s.count(i)-t.count(i)
            if a<0:
                check=0
                break
            else:
                k.append(i)
    if check==0:
        print("NO")
    else:
        for i in t:
            a=k.count(i)-t.count(i)
            for j in range(a):
                k.remove(i)
        if k==t:
            print("YES")
        else:
            print("NO")