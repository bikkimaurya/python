n=int(input())
p=[]
for qwerty in range(n):
    l1=list(map(int,input().split(" ")))
    l2=list(map(int,input().split(" ")))
    s=[l2[j]-l1[j] for j in range(3)]
    count=0
    while(s.count(0)!=3):

        m=max(set(s), key = s.count)
        print(s)
        print(m)
        if(m!=0):
            temp=[]
            inc=0
            for i in s:
                if(i>=m and l1[inc]):
                    temp.append(i-m) 
                else:
                    temp.append(i)
                inc+=1
        else:
            s.sort()
            m=s[-1]
            for i in s:
                if(i>=m):
                    temp.append(i-m) 
                else:
                    temp.append(i)
                    
        s=temp
    p.append(count)

for i in p:
    print(i)