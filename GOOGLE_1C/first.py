n =int(input())
ans=[]

for i in range(n):
    cal=input().split(" ")
    east=int(cal[0])
    north=int(cal[1])
    path=cal[2]
    m_t=len(cal[2])
    nd=path.count("N")
    sd=path.count("S")
    l=abs(north+nd-sd)
    if((east+l)<=m_t):
        temp=north+east
        if(temp%2==0):
            ans.append(max((int(temp/2)),east))
        else:
            ans.append(max(int(temp/2)+1,east))
    else:
        ans.append("IMPOSSIBLE")
c=1
for answer in ans:
    print("Case #"+str(c)+": "+str(answer))
    c+=1