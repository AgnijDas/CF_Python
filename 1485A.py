t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    m=32
    current=0
    for j in range(0,32):
        b1=b+j
        if b1==1:
            continue
        current+=j
        ta=a
        while ta>0:
            ta//=b1
            current+=1
        if current<m:
            m=current
        current=0
    print(m)