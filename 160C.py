n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
m=[]
j=0
count=1
while j<n:
    if j==n-1:
        m.append(count)
    elif l[j]==l[j+1]:
        count+=1
    else:
        m.append(count)
        count=1
    j+=1
j=a=0
while j<n:
    if k>m[a]*n:
        k=k-m[a]*n
    else:
        g=k//m[a]
        if k%m[a]!=0:
            g+=1
        print(l[j],l[g-1])
        break
    j=j+m[a]
    a+=1

