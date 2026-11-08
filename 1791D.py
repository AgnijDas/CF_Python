t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    left=set()
    right={}
    for x in s:
        right[x]=right.get(x,0)+1
    c=0
    for x in right:
        c+=1
    ans=c
    for x in s[:-1]:
        left.add(x)
        right[x]-=1
        if right[x]==0:
            del right[x]
        c=len(left)+len(right)
        ans=max(ans,c)
    print(ans)