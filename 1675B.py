t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    j=opp=0
    check=0
    while j<n-1:
        if l[j]>=l[j+1]:
            if l[j]==0:
                check=1
                print(-1)
                break
            l[j]//=2
            if j!=0:
                j-=1
            opp+=1
        else:
            j+=1
    if check==0:
        print(opp)