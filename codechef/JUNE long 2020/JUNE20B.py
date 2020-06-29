try:
    n=int(input())
    p=[]
    for i in range(n):
        ab=input().split(" ")
        a=int(ab[0])
        b=int(ab[1])
        l=input().split(" ")
        l=list(map(int,l))
        # print(a,b)
        # print(l)
        ans=0
        for i in l:
            if(i>b):
                ans+=(i-b)
        p.append(ans)
    for i in p:
        print(i)
except:
    pass
   
            