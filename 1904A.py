t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    k=[]
    q=[]
    for i in range(2):
        e=y1+b*((-1)**i)
        f=y2+b*((-1)**i)
        for j in range(2):
            c=x1+a*((-1)**j)
            d=x2+a*((-1)**j)
            k.append([c,e])
            q.append([d,f])
    for i in range(2):
        e=y1+a*((-1)**i)
        f=y2+a*((-1)**i)
        for j in range(2):
            c=x1+b*((-1)**j)
            d=x2+b*((-1)**j)
            k.append([c,e])
            q.append([d,f])
    count=0
    for i in k:
        if i in q:
            count+=1
    print(count//2 if a==b else count)
    
