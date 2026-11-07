t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    x=input()
    s=input()
    opp=0
    for i in range(7):
        if s in x:
            print(opp)
            opp=9
            break
        x=x*2
        opp+=1
    if(opp!=9):
        print(-1)
        
