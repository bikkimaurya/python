def drop(l1:list,l2:list):
    flag=False
    for i in l1:
        try:
                l2.remove(i)
                l1.remove(i)
                flag=True
        except:
            pass
    return l1,l2,flag


for q in range(int(input())):
    input()
    cost=0
    l1=list(map(int,input().split(" ")))
    pl2=l2=list(map(int,input().split(" ")))
    flag=True

    for i in list(set(l1+l2)):
        if((l1.count(i)+l2.count(i))%2!=0):
            print(-1)
            break
    else:
        continue


    while(len(l1)!=0):

        # print("l1====================",l1p)
        l1p=tuple()
        l2p=tuple()
        # print("l2====================",l2p)

        l1.sort()
        l2.sort()
        if(l1==l2):
            break
        if(not(flag) and l1p==tuple(l1 )and tuple(l2)==l2p):
            cost=-1
            break
        while(flag):
            l1,l2,flag=drop(l1,l2)

        # print(l1,l2)
        if(len(l1)<1):
            break
        l1[0],l2[0]=l2[0],l1[0]
        cost+=min(l1[0],l2[0])
        l1p=tuple(l1)
        l2p=tuple(l2)

    print(cost)
