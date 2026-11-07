s=input()
t=""
for i in range(len(s)):
    if s[i] not in "aeiouyYAEIOU":
        t=t+"."+s[i].lower()
print(t)