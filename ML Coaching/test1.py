detail={}



def register():
    i=int(input("enter id"))
    name=input("enter name")
    age=int(input("enter age"))
    detail[i]=[name,age]

def search():
    i =int(input("enter you emp id"))
    if i in detail.keys():
        print(detail[i])
    else:
        print("kuchh bhi")





def registerWhile():
    while True:
        register()
        flag=input("Do you want to continue(Y/N)")
        if(flag=="Y"):
            continue
        elif(flag=="N"):
            break

def searchWhile():
    while True:
        search()
        flag=input("Do you want to continue(Y/N)")
        if(flag=="Y"):
            continue
        elif(flag=="N"):
            break



registerWhile()
searchWhile()




