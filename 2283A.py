t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    sum=r*(r+1)//2 - l*(l-1)//2
    if sum>=l and sum<=r:
        print(0)
    else:
        if (l>0 and r>0) or (l<0 and r<0):
            print(r-l)
        elif l==0 or r==0:
            print(r-l-1)
        else:
            print(abs(abs(r)-abs(l))-1)
