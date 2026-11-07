t=int(input())
for i in range(t):
    l=list(input())
    if l.count("0")==len(l) or l.count("1")==len(l):
        print("NET")
    else:
        a=min(l.count("0"),l.count("1"))
        if a%2==1:
            print("DA")
        else:
            print("NET")