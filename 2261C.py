t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=sum([a%2 for a in l])
    if a%2==0 or a>3 or (a==3 and len(l)>a) or len(l)==1 or (a==1 and len(l)>=3):
        print("MOGGITY")
    else:
        print("LARPITY")
        