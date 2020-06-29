def ans(s):
    s=str(s)
    max_=int(s[0])
    r=[]
    total=0
    for i in range(len(s)-1):
        curr=int(s[i])
        next=int(s[i+1])
        if(max_<next):
            max_=next
        if(next==0 and curr!=0):
            r.append(int(s[i]))
        elif(curr>next):
            r.append(curr-next)
            total+=curr-next
        else:
            r.append(0)
    r.append(int(s[-1]))
    return r
final=[]
n=int(input())
for i in range(n):
    s=input()
    r=ans(s)
    l=ans(s[::-1])

    l.reverse()
    a=""

    for  j in range(len(s)):
        a=a+l[j]*"("+s[j]+r[j]*")"
    _="Case #"+str(i+1)+":"
    final.append(_+" "+a)
for i in final:
    print(i)

  