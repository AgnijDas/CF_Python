t=int(input())
for i in range(t):
    a=input()
    b=input()
    c=0
    if a==b:
        print(0)
        continue
    for j in range(1,min(len(a),len(b))+1):
        for k in range(len(a)-j+1):
            if a[k:k+j] in b:
                c=j
                break
    print(len(a)+len(b)-2*c)