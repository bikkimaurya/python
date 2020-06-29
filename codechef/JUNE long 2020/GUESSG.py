
n=int(input())
inc=0
inc+=1

gel=""
temp=n
top=n
bottom=0
temp=int((top+bottom)/2)
while(True):
    
    flag=False
    ltemp=[]
    for i in range(3):
        print(temp,flush=True)
        gel=input()
        if(gel=="E"):
            flag=True
            break
        
        ltemp.append(gel)
        if(gel==ltemp[0] and i):
            break
    if(flag):
        break

    gel=max(set(ltemp), key = ltemp.count) 

    if(0<top-bottom<2):
        print(top,flush=True)
        gel=input()
        if(gel=="E"):
            break
        else:
            print(bottom,flush=True)
            gel=input()
            if(gel=="E"):
                break
    # print(top,bottom)
    elif(gel=="E"):
        term=True
        break
    elif(gel=="L"):                
        top=temp
        if(top>n):
            top=n+i
        
            

        temp=int((abs(top+bottom))/2)
    elif(gel=="G"):
        bottom=temp
        temp=int((top+bottom)/2)
    


