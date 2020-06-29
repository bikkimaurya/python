try:
    qwe=int(input())
    printer=[]
    for qwerty in range(qwe):
        ts=int(input())
        ans=0
        # print(ts)
        for i in range(2,ts+1,2):
            # print("for")
            d={2:20,4:2,6:1,8:3,0:1}
            tom=ts
            jerry=i
            # if(tom%2==0):
            #     break
            # print(tom,jerry)

            if(tom%2!=0 and jerry%2==0):
                ans+=1
                continue
            

            if(tom<20 or jerry<20):
                while(tom%2==0 and jerry%2==0):
                    # print("while")
                    tom=int(tom/2)
                    jerry=int(jerry/2)
                    if(tom%2!=0 and jerry%2==0):
                        ans+=1
                continue
            tom=int(str(tom)[-1])
            jerry=int(str(jerry)[-1])

            if(d[jerry]>d[tom]):
                ans+=1
                # print("this is the case")
            
        printer.append(ans)

    for i in printer:
        print(i)
except:
    pass
                