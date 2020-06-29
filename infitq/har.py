def harshad(n):
    s=sum(list(map(int,str(n))))
    if(n%s==0):
        return True
    return False

row=int(input())
mat=[]
for i in range(row):
    mat.append(list(map(int,input().split(","))))


col=len(mat[0])
v=0
for i in range(row-1):
    for j in range(col-1):
        if(harshad(mat[i][j]) and harshad(mat[i][j+1]) and harshad(mat[i+1][j]) and harshad(mat[i+1][j+1])):
            print("{}{}".format((mat[i][j]),(mat[i][j+1])))
            print("{}{}".format((mat[i+1][j]),(mat[i+1][j+1])))
            v=1
if(v==0):
    print("-1")

        