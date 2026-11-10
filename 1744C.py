t=int(input())
for j in range(t):
    n,c=map(str,input().split())
    n=int(n)
    s=input()
    if c=="g":
        print(0)
    else:
        m=s.index(c)
        s=s+s[:s.index("g")+1]
        t=0
        check=0
        for i in range(m+1,len(s)):
            if s[i]=="g" and check==0:
                g=i
                if g-m>t:
                    t=g-m
                check=1
            elif s[i]==c and check==1:
                m=i
                check=0
        print(t)

    

    