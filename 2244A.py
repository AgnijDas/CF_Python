t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    m=0
    count=0
    for i in s:
        if i=="#":
            count+=1
        else:
            if count>m:
                m=count
            count=0
    if count>m:
        m=count
    print(m//2+m%2)