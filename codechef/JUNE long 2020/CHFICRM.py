try:
    n=int(input())
    p=[]
    for qwerty in range(n):
        ab=input()
        l=input().split(" ")
        l=list(map(int,l))
        
        if(l[0]>6):
            p.append("NO")
        else:    
            avail=[]
            flag=True
            for i in l:
                # print(avail)
                r=i-5
                if(i==5):
                    avail.append(5)
                    continue
                elif (i==15 and avail.count(10)>=1):
                    avail.pop(avail.index(10))
                    
                elif(i==15 and avail.count(5)>=2):
                    avail.pop(avail.index(5))
                    avail.pop(avail.index(5))
                    continue

                
                elif(avail.count(5)>0 and i==10):
                    avail.append(10)
                    avail.pop(avail.index(5))
                elif(avail.count(r)==0) :
                    p.append("NO")
                    flag=False
                    break

            if(flag):
                p.append("YES")
            
    for i in p:
        print(i)
except:
    pass