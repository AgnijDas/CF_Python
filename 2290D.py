t=int(input())
for i in range(t):
    n=int(input())
    l=list(input())
    d={}
    for x in l:
        d[x]=ord(x)
    for j in range(n//2):
        a=d[l[j]]
        b=d[l[n-1-j]]
        if a!=b:
            for k in d.keys():
                if d[k]==max(a,b):
                    d[k]=min(a,b)
    opp=0
    for j in sorted(d.keys(),reverse=True):
        if d[j]<ord(j):
            if opp==0:
                opp+=ord(j)-d[j]
                low=d[j]
            elif ord(j)>low and d[j]<low:
                opp+=low-d[j]
                low=d[j]
            elif ord(j)<low:
                opp+=ord(j)-d[j]
                low=d[j]
    print(opp)