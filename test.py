amount=0
while True:
    
    temp = input("input ")
    if(temp=="bye"):
        print(amount)
        break
    wd=temp.split(" ")
    w=wd[0]
    d=int(wd[1])
    if(w=="W"):
        amount-=d
    elif(w=="D")::
        amount+=d
        

    

