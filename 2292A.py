t=int(input())
for i in range(t):
    l,a,b=map(int,input().split())
    st=[]
    bl=[]
    start=0
    while True:
        if start not in st:
            st.append(start)
            start=(start+a)%l
        else:
            break
    start=0
    while True:
        if start not in bl:
            bl.append(start)
            start=(start+b)%l
        else:
            break
    c=0
    for i in st:
        if i in bl:
            c+=1
    print(c)
    