def div(n):
    c=n
    while c>0:
        d=c%10
        c=c//10
        if d==0:
            continue
        elif n%d!=0:
            return False
    return True
t=int(input())
for i in range(t):
    n=int(input())
    while True:
        if div(n):
            break
        else:
            n+=1
    print(n)