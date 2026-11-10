n,d=map(int,input().split())
p=list(map(int,input().split()))
rem=n
j=0
t=0
p.sort(reverse=True)
while True:
    if j<=n-1 and ((d//p[j])+1<=rem):
        t+=1
        rem=rem-(d//p[j]+1)
        j+=1
    else:
        break
print(t)

    