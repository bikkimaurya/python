# 0 chef
# 1 morty
# 2 drow
for i in range(int(input())):
    n=int(input())
    chef=0
    morty=0
    drow=0
    for i in range(n):
        l=input().split(" ")
        l1=list(l[0])
        l2=list(l[1])
        a=sum(list(map(int,l1)))
        b=sum(list(map(int,l2)))
        # print(" =====================    ",a,b)

        if(a>b):
            chef+=1
        elif(a<b):
            morty+=1
        else:
            chef+=1
            morty+=1
    # print("+++++++++++++++++++++",chef,morty)
    ans=0
    point=chef
    if(chef<morty):
        ans=1
        point=morty
    elif (chef==morty ):
        ans=2
    print(ans,point)

