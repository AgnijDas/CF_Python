t=int(input())
for i in range(t):
    l=list(input())
    a=l.count("1")
    b=len(l)-a
    if a==b:
        print(0)
    else:
        j=0
        while True:
            if l[j]=="0":
                if a>=1:
                    a-=1
                else:
                    break
            else:
                if b>=1:
                    b-=1
                else:
                    break
            j+=1
        print(a+b)