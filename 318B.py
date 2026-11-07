s=input()
h=0
c=0
for i in range(len(s)-4):
    if s[i:i+5]=="heavy":
        h+=1
    elif s[i:i+5]=="metal":
        c+=h
print(c)
