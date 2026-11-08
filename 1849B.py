t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l=[j%k if j%k!=0 else k for j in l ]
    g=[]
    for j in range(n):
        g.append([l[j],j])
    g.sort(key=lambda x:(-x[0], x[1]))
    for j in range(n):
        print(g[j][1]+1,end=" ")
    print()