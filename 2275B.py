t=int(input())
for i in range(t):
    n=int(input())
    l=input()
    l=[int(j) for j in l]
    rem=[]
    mem=[]
    for j in range(len(l)):
        if l[j]==3:
            rem.append(j+1)
        elif l[j]==2:
            if len(mem)!=0:
                rem.append(mem[-1])
                mem.pop(-1)
            else:
                rem.append(j+1)
        else:
            mem.append(j+1)
    print(n-len(rem))
    rem=set(rem)
    print(*[j for j in range(1,n+1) if j not in rem])

    