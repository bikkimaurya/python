import sys
# n=int(input())
try:
    n=int(sys.stdin.readline())
    gel=""
    temp=n
    temp=int(temp/2)
    while(True):
        
        print(temp)
        # sys.stdout.flush(temp)
        fist=prev=gel=input()
        term=lied=False
        
        if(not(lied)):
            for i in range(2):
                incr=True
                if(prev!=gel):
                    lied=True
                if(gel=="E"):
                    term=True
                    break
                if((prev==gel and i!=0) or (fist==gel and i==1) and incr):
                        incr=False
                        if(gel=="E"):
                            break
                        elif(gel=="G"):
                            temp=int(temp/2)
                        elif(gel=="L"):
                            temp=2*temp-(int(temp/2))
                        break
                
                prev=gel
    
                print(temp)
                # sys.stdout.flush(temp)
                gel=input()
        elif(term==True):
            break
        else:
            if(gel=="E"):
                break
            elif(gel=="G"):
                temp=int(temp/2)
            elif(gel=="L"):
                temp=2*temp-int((temp/2))
    
        
except:
    pass
