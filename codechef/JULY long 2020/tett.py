t=int(input())
for i in range(t):
    x=int(input())
    if(x%3 ==0 or x%7 ==0 or x%(10)==0):
        print("YES")
    else:
        w3=x%3
        w7=x%7
        if(w3%7 ==0):
            print("YES")
        elif (w7%3==0):
            print("YES")
        else:
            print("NO")
