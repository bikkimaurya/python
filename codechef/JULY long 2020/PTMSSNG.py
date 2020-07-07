x=[]
y=[]
f=[]
for q in range(int(input())):
    x=[]
    y=[]
    f=[]
    for i in range( (4*int(input())) - 1):
        ab=input().split(" ")
        x.append(int(ab[0]))
        y.append(int(ab[1]))
        f.append("")
    for i in range(0,len(x)):
        curr_x=x[i]
        curr_y=y[i]
        for j in range(i+1,len(x)):
            if(x[j]==curr_x):
                f[j]+="x"
                f[i]+="x"
            if(y[j]==curr_y):
                f[j]+="y"
                f[i]+="y"
    a=""
    b=""

    for i in range(0,len(x)):
        if(f[i]=="x"):
            b=y[i]
        elif (f[i]=="y"):
            a=x[i]
    print(a,b)

