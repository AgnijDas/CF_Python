import sys
t=int(input())
for i in range(t):
    l = [list(input()) for _ in range(10)]
    p=0
    for k in range(5):
        for m in range(k,10-k):
            for j in range(k,10-k):
                if l[m][j]=="X":
                    p+=1
    print(p)
                
