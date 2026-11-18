t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    count=0
    for j in s:
        if j==".":
            count+=1
        else:
            count=0
        if count==3:
            break
    if count==3:
        print(2)
    else:
        print(s.count("."))
