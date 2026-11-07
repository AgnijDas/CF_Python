t=int(input())
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    count=1 if l[0]==0 else 0
    for i in range(1,n):
        if l[i]==0 and l[i-1]==0:
            continue
        elif l[i]==0:
            count+=1
    if l[0]==0 and l[-1]==0:
        count=count-1
    elif l[0]==0 or l[-1]==0:
        count=count
    else:
        count=count+1
    print(min(count,2))