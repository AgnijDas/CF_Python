t=int(input())
for i in range(t):
    n=int(input())
    l=list(input())
    a=0
    opp=0
    for i in l:
        if i==")":
            a-=1
            if a==-1:
                opp+=1
                a=0
        else:
            a+=1
    print(opp)