t=int(input())
for i in range(t):
    n,r,b=map(int,input().split())
    if b==1:
        if r%2==0:
            print("R"*(r//2)+"B"+"R"*(r//2))
        else:
            print("R"*(r//2+1)+"B"+"R"*(r//2))
        continue
    a=r//(b+1)
    rem=r%(b+1)
    for j in range(b):
        if rem>=1:
            print("R"*(a+1)+"B",sep="",end="")
            rem-=1
        else:
            print("R"*a+"B",sep="",end="")
    print("R"*a)
    
    


    