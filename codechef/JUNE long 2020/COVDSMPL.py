q=int(input())
for _ in range(q):


    
    
    count=0
    
    nm=list(map(int,input().split(" ")))
    n=nm[0]
    m=nm[1]
    l1=[[0 for i in range(n)] for j in range(n)]

    print(1,1,1,n,n,flush=True)
    maxm=int(input())
    flag=False
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(1,i,j,i,j,flush=True)
            temp=int(input())
            if(temp==1):
                count+=1
                l1[i-1][j-1]=1
            if(count==maxm):
                flag=True
                break
        if(flag):
            break
    print(2,flush=True)
    for i in l1:
        for j in i:
            print(j,end=" ",flush=True)
        print(flush=True)
    term=int(input())
    if(term==-1):
        break
        







