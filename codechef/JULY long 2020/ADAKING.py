for q in range(int(input())):
    r=p=int(input())
    l=[["X" for i in range(0,8)] for i in range(0,8)]
    si=0
    sj=0
    for i in range(min(int(p/8)+1,8)):
        for j in range(0,8):
            if(r!=0):
                l[i][j]="."
                r-=1        
    
    l[0][0]="O"
    for i in l:
        for j in i:
            print(j,end="")
        print()
    print()