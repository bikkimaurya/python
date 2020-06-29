
def findanswer2(p,q,r,a,b,c):
    temp=1
    add=(p*b-a*q)
    if((p-q)==0 and (add%(p-q))!=0):
        return 0

    add/=(p-q)
    add=int(add)
    sub=a-add
    if(p==0 or(sub%(p))!=0):
        return 0
    sub/=p
    sub=int(sub)
    p1=p
    q1=q
    r1=r
    r+=add
    if(r==c):

        temp+=1
        return temp

    p=p1
    q=q1
    r=r1
    r*=sub

    if(r==c):
        temp+=1
        return temp
    p=p1
    q=q1
    r=r1
    r=r*sub+add
    if(r==c):
        temp+=1
        return temp



    p=p1
    q=q1
    r=r1
    sub=a-b
    if((p-q)==0 or (sub%(p-q))!=0):
        return 0
    sub/=(p-q)
    
    sub=int(sub)
    add=a
    if(sub==0 or (add%(sub))!=0):
        return 0
    add/=sub
    add=int(sub)
    add-=p
    r+=add
    if(r==c):
        temp+=1
        return temp
    p=p1
    q=q1
    r=r1
    r*=sub
    if(r==c):
        temp+=1
        return temp
    p=p1
    q=q1
    r=r1
    r=(r+add)*sub

    if(r==c):
        temp+=1
        return temp
    return 0



def findanswer(p,q,r,a,b,c):

    temp=1
    diff=c-r
    if(a==0 and b==0):
        temp+=1
        return temp 
    if((p-a)==q-b):
        temp+=1 
        return temp 
    if((p!=0) and(a%p)==0 and(q!=0) and(b%q)==0):
         if(a/p==b/q):
            temp+=1 
            return temp 
    p1=p
    q1=q
    r1=r 
    p+=diff 
    if((p-a)==q-b):

        temp+=1 
        return temp 
    if((p!=0) and(a%p)==0 and(q!=0) and(b%q)==0):
        if(a/p==b/q):
            temp+=1 
            return temp 



            
    p=p1
    q=q1
    r=r1 
    q+=diff 
    if((p-a)==q-b):
        temp+=1 
        return temp
    if((p!=0) and(a%p)==0 and(q!=0) and(b%q)==0):
        if(a/p==b/q):
            temp+=1 
            return temp 
    p=p1
    q=q1
    r=r1 
    p+=diff 
    q+=diff 
    if((p-a)==q-b):
        temp+=1 
        return temp
    if((p!=0) and(a%p)==0 and(q!=0) and(b%q)==0):
           if(a/p==b/q):
                temp+=1 
                return temp 
    p=p1,q=q1,r=r1 
    if((r!=0) and(c%r)==0):

        mult=int(c/r)
        if((p-a)==q-b):

            temp+=1 
            return temp 
        if((p!=0) and(a%p)==0 and(q!=0) and(b%q)==0):
            if(a/p==b/q):
                temp+=1 
                return temp 
        p=p1,q=q1,r=r1 
        p*=mult 
        if((p-a)==q-b):
            temp+=1 
            return temp 
        if((p!=0) and(a%p)==0 and(q!=0) and(b%q)==0):
            if(a/p==b/q):
                temp+=1 
                return temp 

        p=p1
        q=q1
        r=r1 
        q*=mult 
        if((p-a)==q-b):
            temp+=1 
            return temp 
        if((p!=0) and(a%p)==0 and(q!=0) and(b%q)==0):
            if(a/p==b/q):
                temp+=1 
                return temp 
        p=p1
        q=q1
        r=r1 
        p*=mult 
        q*=mult 
        if((p-a)==q-b):
            temp+=1 
            return temp 
        if((p!=0) and(a%p)==0 and(q!=0) and(b%q)==0):
            if(a/p==b/q):
                temp+=1 
                return temp 
    
    return 0 


def sol():


    p=q=r=a=b=c=""
    l1=list(map(int,input().split(" ")))
    l2=list(map(int,input().split(" ")))

    p=l1[0]
    q=l1[1]
    r=l1[2]
    a=l2[0]
    b=l2[1]
    c=l2[2]

    if(p==a and q==b and r==c):
        print(0)
        return
    if(a==0 and b==0 and c==0):
        print(1) 
        return 
    if((p-a)==q-b and(q-b)==r-c):
        print(1)
        return 
    if((p!=0) and (a%p)==0 and(q!=0) and(b%q)==0 and(r!=0) and(c%r)==0):
        if(a/p==b/q and b/q==c/r):
            print(1)
            return 
    if((p!=a and q==b and r==c) or (p==a and q!=b and r==c) or (p==a and q==b and r!=c)):
        print(1)
        return 
    if(p!=a and q!=b and r==c):
        if(a==0 and b==0):
            print(1)
            return 
        if((p-a)==q-b):
            print(1)
        if((p!=0) and(a%p)==0 and(q!=0) and(b%q)==0):
            if(a/p==b/q):
                print(1)
                return 
        print(2)
        return 
    if(p!=a and q==b and r!=c):
        if(a==0 and c==0):

            print(1)
            return 
        if((p-a)==r-c):
            print(1)
            return
        if((p!=0) and(a%p)==0 and(r!=0) and(c%r)==0):
            if(a/p==c/r):
                print(1)
                return 
        print(2)
        return 
    if(p==a and q!=b and r!=c):
        if(b==0 and c==0):
            print(1)
            return 
        if((q-b)==r-c):
            print(1)
    print(2)


for _ in range(int(input())):
    sol()