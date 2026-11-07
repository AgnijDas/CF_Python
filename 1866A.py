n=int(input())
l=list(map(int,input().split()))
d=max(l)
for i in l:
    if abs(i)<d:
        d=abs(i)
print(abs(d))
