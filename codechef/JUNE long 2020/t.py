try:
    n=int(input())
    
    def gcd(a,b):

        if (b == 0):
            return a
        if (a==0):
            return b
        else:
            return gcd(b, a%b)

    for qwerty in range(n):
        l1=list(map(int,input().split(" ")))
        l2=list(map(int,input().split(" ")))
        s=[l2[j]-l1[j] for j in range(3)]
        if(l1>l2):
            print("0")
            continue
        count=0
        while(s.count(0)!=3):
            g=gcd(s[0],gcd(s[1],s[2]))
            # temp=0
            for i in range(3):
                # if(int(l1[i]/g)<=l2[i] or s[i]==0):
                #     temp+=1
                if(s[i]-g>=0):
                    s[i]=s[i]-g
                else:
                    s[i]=s[i]
            # if(temp==3):
            count+=1
            # else:
            #     count+=g
        print(count)
except:
    pass