n=int(input())
l=list(map(int,input().split()))
if n==1:
    print(0)
else:
    i=1
    j=n-2
    s1=l[0]
    s2=l[-1]
    equal=s1 if s1==s2 else 0
    while i<=j:
        if s1>s2:
            s2+=l[j]
            j-=1
        else:
            s1+=l[i]
            i+=1
        if s1==s2:
            equal=s1
    print(equal)

    