def mid(l):
    left=[]
    right=[]
    for i in l:
        v=i.split("*")
        left.append(v[0]+"*")
        right.append("*"+v[1])
    print(left)
    print(right)
    l=fl(left)
    r=fl(right)
    print(l+"  "+r)
    if(l!="*" and r!="*"):
        return l+r
    elif(l!="*" and r=="*"):
        return l
    elif(l=="*" and r!="*"):
        return r
    else :
        return "*"
    










def fl(l):
    l.sort(key=len)
    #print(l)
    count=0
    for i in range(len(l)-1):
        if(l[i]==""):
            count+=1
            continue
        
        t=l[i].split("*")
        t.remove("")
        curr=t[0]

        t=l[i+1].split("*")
        t.remove("")
        nxt=t[0]
        
        temp=len(curr)*-1
        f=nxt[temp::]
        #print("f is ",f)
        #print("cuur os ",curr)
        if ( f==curr):
            count+=1
    #print(count)
    if(count+1==len(l)):
        t=l[len(l)-1].split("*")
        t.remove("")
        return t[0]

    else:
        return "*"


ans=[]
n=int(input())
for i in range(n):
    m=int(input())
    l=[]
    count=0
    count_=0
    for i in range(m):

        #b=[]
        v=input()
        #b.append(v)
        #re=v.split("*")
        #re.remove("")

        #lnt=len(re)
        
        #b.append(lnt)
        #l.append(b)
        l.append(v)

        if(v[0]=="*" or v[-1]=="*"):
            count+=1
    #print(count,"  ",len(l))

    if(count==len(l)):
        ans.append(fl(l))
    else:
        ans.append(mid(l))
c=1
for i in ans:
    print("Case #"+str(c)+": "+ i)
    c+=1





