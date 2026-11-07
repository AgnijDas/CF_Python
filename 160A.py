n=int(input())
a=list(map(int, input().split()))
a.sort()
count=1
for i in range(n):
    s=0
    for j in range(count):
        s+=a[n-1-j]
    if (s>(sum(a)-s)):
        break
    else:
        count+=1
print(count)
        
