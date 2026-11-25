n,k=map(int,input().split())
l=list(map(int,input().split()))
a=l[k-1]
count=0
for i in l:
    if i>=a and i>0:
        count+=1
print(count)