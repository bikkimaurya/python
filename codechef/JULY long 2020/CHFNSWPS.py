try:
    for q in range(int(input())):
        ans=0
        input()
        l1=list(map(int,input().split(" ")))
        l2=list(map(int,input().split(" ")))
        l=l1+l2
        u=list(set(l))
        # print(u)
        # l1u=[]
        # l2u=[]
        for i in u:
            l1c=l1.count(i)
            l2c=l2.count(i)
            if((l1c+l2c)%2==0):
                t=int(abs(l1c-l2c)/2)
                ans+=t
            else:
                ans=-1
                print(-1)
                break
        else:
            print(int(ans/2))
except:
    pass
        
