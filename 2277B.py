t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if 0 in l:
        print(len(l))
    elif n==1:
        print(0)
    else:
        l.sort()
        check=0
        for i in range(n):
            if len(l)-1>=l[i]:
                print(len(l))
                check=1
                break
        if check==0:
            print(0)
