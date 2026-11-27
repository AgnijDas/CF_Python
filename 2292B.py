t=int(input())
for i in range(t):
    n,k,p=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    count=0
    s=0
    jc=0
    juice=0
    for j in l:
        if count<k:
            s+=j
            count+=1
        else:
            if s<p:
                juice+=s
                jc+=1
            count=1
            s=j
    if count==k and s<p:
        juice+=s
        jc+=1
    print(sum(l)-juice+jc*p)
    