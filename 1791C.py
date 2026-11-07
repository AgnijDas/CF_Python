t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    while True:
        if len(s)<2 or s[-1]==s[0] :
            break
        else:
            s=s[1:n-1]
            n=n-2
    print(len(s))
