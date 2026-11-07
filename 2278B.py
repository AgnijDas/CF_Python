t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x>=y and x>=z:
        print("P"*(x+y+z))
    elif y>=x and y>=z:
        print("R"*(x+y+z))
    else:
        print("S"*(x+y+z))