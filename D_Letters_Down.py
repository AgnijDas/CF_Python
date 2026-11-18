t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    d={}
    opp=0
    for j in range(n//2):
        a=d.get(s[j],ord(s[j]))
        b=d.get(s[-j-1],ord(s[-j-1]))
        if a>b:
            d[s[j]]=b
            opp+=a-b
        elif b>a:
            d[s[-j-1]]=a
            opp+=b-a
    print(opp)
        
            