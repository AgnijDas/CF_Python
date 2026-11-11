n=int(input())
l=list(map(int,input().split()))
l.sort()
check=0
for i in range(n-2):
    if l[i]+l[i+1]>l[i+2]:
        check=1
        break
if check==1:
    print("YES")
else:
    print("NO")