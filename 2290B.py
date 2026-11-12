t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    count=0
    current=s[0]
    if current=="B":
        count+=1
    for i in s:
        if current!=i:
            count+=1
            current=i
        current="R" if current=="B" else "B"
    print(count)