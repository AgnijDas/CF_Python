t=int(input())
for j in range(t):
    n,c=map(str,input().split())
    s=list(input())
    n=int(n)
    a=0
    for i in range(n//2):
        if s[i]==s[-i-1]:
            continue
        else:
            if s[i]==c or s[-i-1]==c:
                a+=1
            else:
                a+=2
    print(a)