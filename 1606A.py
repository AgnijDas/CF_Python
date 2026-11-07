t=int(input())
for i in range(t):
    l=list(input())
    a=b=0
    for i in range(len(l)-1):
        c=l[i]+l[i+1]
        if c=="ab":
            a+=1
        elif c=="ba":
            b+=1

    if a>b:
        print("b"+''.join(l[1:]))
    elif b>a:
        print("a"+''.join(l[1:]))
    else:
        print(''.join(l))
