n=int(input())
for i in range(n):
    a,c,b=map(int,input().split())
    if(b%2==0):
        if c>=a:
            print("Second")
        else:
            print("First")
    else:
        if a>(c-1) :
            print("First")
        else:
            print("Second")
        
