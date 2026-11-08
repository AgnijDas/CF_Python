t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d1={}
    d2={}
    f=1
    g=1
    for i in range(n-1):
        if a[i]==a[i+1]:
            f+=1
        else:
            if a[i] in d1.keys():
                if f>d1[a[i]]:
                    d1[a[i]]=f
            else:
                d1[a[i]]=f
            f=1
        if b[i]==b[i+1]:
            g+=1
        else:
            if b[i] in d2.keys():
                if g>d2[b[i]]:
                    d2[b[i]]=g
            else:
                d2[b[i]]=g
            g=1
    if a[-1] in d1.keys():
        if f>d1[a[-1]]:
            d1[a[-1]]=f
    else:
        d1[a[-1]]=f
    if b[-1] in d2.keys():
        if g>d2[b[-1]]:
            d2[b[-1]]=g
    else:
        d2[b[-1]]=g
    c=0
    for j in d1.keys():
        if j in d2.keys():
            if d1[j]+d2[j]>c:
                c=d1[j]+d2[j]
        elif d1[j]>c:
            c=d1[j]
    if max(d2.values())>c:
        c=max(d2.values())
    print(c)