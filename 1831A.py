t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    b=[]
    for j in range(n):
        b.append(n+1-l[j])
    for j in b:
        print(j,end=" ")
