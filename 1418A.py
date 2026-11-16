import math
t=int(input())
for i in range(t):
    x,y,k=map(int,input().split())
    print((k+k*y+x-3)//(x-1)+k)

# In python, to avoid floating point precision errors, for math.ceil(a/b) use (a+b-1)//b