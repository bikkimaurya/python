try:
    n=int(input())
    p=[]
    for qwery in range(n):
        s=input()
        ans=0
        i=0
        while(i<len(s)-1):
            current=s[i]
            n=s[i+1]
                

            if((current=="y" and n=="x") or (current=="x" and n=="y")):
                ans+=1
                # print(i,end="") 
                i+=1
                # print(i)
            i+=1
        p.append(ans)

    for i in p:
        print(i)
except:
    pass

   
            