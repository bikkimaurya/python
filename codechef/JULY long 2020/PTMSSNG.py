for q in range(int(input())):
    x=[]
    y=[]
    for i in range( (4*int(input())) - 1):
        ab=input().split(" ")
        a=int(ab[0])
        b=int(ab[1])
        if(a in x):
            x.remove(a)
        else:
            x.append(a)
        if(b in y):
            y.remove(b)
        else:
            y.append(b)
    print(x[0],y[0])
