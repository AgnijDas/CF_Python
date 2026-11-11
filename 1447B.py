t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    l=[]
    pos_index=0
    neg=[]
    zero=0
    for j in range(m):
        l.extend(list(map(int,input().split())))
    l.sort()
    for j in range(len(l)):
        if l[j]>0:
            pos_index=j
            break
        elif l[j]==0:
            zero+=1
        else:
            neg.append(l[j])
    if len(neg)+zero==len(l):
        if len(neg)%2==0 or zero>=1:
            print(-sum(neg))
        else:
            print(-sum(neg)+2*neg[-1])
        continue
    s=sum(l[pos_index:]) 
    if len(neg)%2==0 or zero>=1:
        print(s-sum(neg))
    else:
        if abs(neg[-1])>l[pos_index]:
            print(s-sum(neg)-2*l[pos_index])
        else:
            print(s-sum(neg)+2*neg[-1])




        
            

        
