for q in range(int(input())):
    r=p=int(input())
    l=[["." for i in range(0,8)] for i in range(0,8)]
    # print(p)
    si=0
    sj=0
    # print(int(p/8)+1,"========================----+")
    for i in range(min(int(p/8)+1,8)):
        # print("=======")
        for j in range(0,8):
            if(r!=0):
                l[i][j]="."
                r-=1
            else:
                l[i][j]="X"
                si=i
                sj=j
                break
    print(si,sj,"99999999999999999999999")
    if(si+1<8 and sj<8 and sj!=0):
        for j in range(0,sj+1):
            l[si+1][j]="X"

        if(int(p/8)>0):
            for j in range(sj,8):
                l[si][j]="X"

                
    
    l[0][0]="O"
    for i in l:
        for j in i:
            print(j,end=" ")
        print()

