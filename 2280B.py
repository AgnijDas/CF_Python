import sys
t=int(input())
for i in range(t):
    n=int(input())
    print("?",1,n,flush=True)
    a=int(input())
    if a==-1:
        sys.exit()
    if a==n or a==0:
        print("! NO",flush=True)
    else:
        print("?",a+1,n,flush=True)
        b=int(input())
        if b==-1:
            sys.exit()
        if b==0:
            print("! NO",flush=True)
        else:
            print("! YES",flush=True)

