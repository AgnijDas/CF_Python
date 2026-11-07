t=int(input())
for i in range(t):
    n=int(input())
    digit=len(str(n))
    m=digit
    a=b=c=d=0
    #a-2,b-5,c-0,d-7
    while digit>0:
        e=n%10
        n=n//10
        if e==0:
            if c!=0:
                print(m-digit-1)
                break
            else:
                c=digit
        if e==2:
            if b!=0:
                print(m-digit-1)
                break
            elif a==0:
                a=digit
        if e==5:
            if c!=0:
                print(m-digit-1)
                break
            elif b==0:
                b=digit
        if e==7:
            if b!=0:
                print(m-digit-1)
                break
            elif d==0:
                d=digit
        digit-=1
                    