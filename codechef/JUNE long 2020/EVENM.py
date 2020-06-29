try:
    q=int(input())
    for qwerty in range(q):
        n=int(input())
        l=[]
        last=1
        for i in range(0,n):
            l2=[j for j in range(last,last+n)]
            
            
            if(i%2!=0 and n%2==0):
                l2.reverse()
                l.append(l2)
            else:
                l.append(l2)
            last+=n
        
        for i in l:
            for j in i:
                print(j,end=" ")
            print()
            
except:
    pass
