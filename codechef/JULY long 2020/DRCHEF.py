import bisect
for qwerty in range(int(input())):
    nx=input().split(" ")
    n=int(nx[0])
    x=int(nx[1])
    l=list(map(int,input().split(" ")))
    l.sort()
    left=bisect.bisect_left(l,x)
    # left=left-l[0]
    day=0


    for i in range(left,len(l)):
        if(x<l[i]):
            while(x<l[i]):
                x*=2
                day+=1
            day+=1
        else:
            day+=1
        x=2*l[i]
    prev=left+day
    if(left!=0):
        day=0
        left-=1
        for i in range(left,n):
            if(x<l[i]):
                while(x<l[i]):
                    x*=2
                    day+=1
                day+=1
            else:
                day+=1
            x=2*l[i]
    if(day+left<prev):
        prev=day+left
    print(prev)
        