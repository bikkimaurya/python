m=int(input())
ans=[]
for i in range(m):
    l=[]
    dia=0
    r=0
    c=0
    n=int(input())
    for j in range(n):
        v=list(map(int,input().split(" ")))
        l.append(v)
        dia=dia+int(v[j])
        if(len(set(v))!=len(v)):
            r+=1

    t=zip(*l)
    for i in t:
        if(len(set(i))!=len(i)):
            c+=1
    ans.append(dia)
    ans.append(r)
    ans.append(c)
c=1
for i in range(0,len(ans)-2,3):
    s="Case #"+str(c)+":"
    print(s,ans[i],ans[i+1],ans[i+2],sep=" ")
    c=c+1
    