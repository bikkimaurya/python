m=int(input())
dia_=[]
r_=[]
c_=[]
for i in range(m):
    l=[]
    dia=0
    r=0
    c=0
    n=int(input())
    for j in range(n):
        v=input().split(" ")
        l.extend(v)
        dia=dia+int(v[j])
        if(len(set(v))!=len(v)):
            r+=1

    for j in range(n):
        t=[]
        for k in range(0,len(l),n):
            if(k+j>=len(l)):
                break
            t.extend(l[k+j])
        if(len(set(t))!=len(t)):
            c+=1  
    dia_.append(dia)
    r_.append(r)
    c_.append(c)
for i in range(m):   
    print("Case #"+str(i+1)+": "+str(dia_[i])+" "+str(r_[i]) +" "+str(c_[i]))
