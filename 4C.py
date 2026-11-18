n=int(input())
l=[]
otp=[]
data=dict()
for i in range(n):
    a=input()
    if a in l:
        data[a]+=1
        otp.append(a+str(data[a]))
    else:
        l.append(a)
        data[a]=0
        otp.append("OK")
for i in otp:
    print(i)
