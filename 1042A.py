n=int(input())
m=int(input())
l=[]
for j in range(n):
    l.append(int(input()))
l.sort()
a=l[-1]
j=0
copy=m
while copy>0 and j<n:
    copy=copy-(a-l[j])
    l[j]=a
    j+=1
m1=a
if copy>0:
    m1=a+copy//n
    if copy%n!=0:
        m1+=1
print(m1,a+m)
            

