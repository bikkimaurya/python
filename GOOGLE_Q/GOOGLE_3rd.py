m=int(input())

final=[]

for i in range(m):
    cstart=jstart=cend=jend=0
    ans=[]
    l=list()
    t=int(input())
    for i in range(t):
        ll=list(map(int,input().split(" ")))
        ll.append(i)
        l.append(ll)
    l.sort()
    cstart=l[0][0]
    cend=l[0][1]
    lm=[]
    lm.append(l[0][2])
    lm.append("C")
    ans.append(lm)
    s=""
    for j in range(1,t):
        if(not(cstart<=l[j][0]<cend)):
            ll=[]
            ll.append(l[j][2])
            ll.append("C")
            cstart=l[j][0]
            cend=l[j][1]
            
            ans.append(ll)
        elif(not(jstart<=l[j][0]<jend)):
            ll=[]
            jstart=l[j][0]
            ll.append(l[j][2])
            ll.append("J")
            jend=l[j][1]
            
            ans.append(ll)
        else:
            s="IMPOSSIBLE"
            break
    if(len(s)>0):
        final.append(s)
    else:
        ans.sort()
        f=""
        for i in ans:
            f+=i[1]
        final.append(f)
q=1
for i in final:
    print("Case #"+str(q)+": "+i)
    q+=1
