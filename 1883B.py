t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=input()
    even=odd=0
    for j in list(set(s)):
        if s.count(j)%2==0:
            even+=s.count(j)
        elif s.count(j)%2==1 and s.count(j)>2:
            even+=s.count(j)-1
            odd+=1
        else:
            odd+=s.count(j)
    if even>=(n-k):
        print("YES")
    elif (n-k)%2==1 and (even+1)==(n-k) :
        print("YES")
    else:
        print("NO")