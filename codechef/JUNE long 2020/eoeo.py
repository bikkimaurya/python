try:
    qwe=int(input())
    printer=[]
    for qwerty in range(qwe):
        ts=int(input())
        ans=0
        # print(ts)
        for i in range(2,ts+1,2):
            # print("for")
            tom=ts
            jerry=i
            if(tom%2!=0 and jerry%2==0):
                ans+=1
            while(tom%2==0 and jerry%2==0):
                # print("while")
                tom=int(tom/2)
                jerry=int(jerry/2)
                if(tom%2!=0 and jerry%2==0):
                    # print("if")
                    ans+=1

        printer.append(ans)

    for i in printer:
        print(i)
except:
    pass
            