try:
    qw=int(input())
    ans=[]
    for werty in range(qw):
        tom=int(input())
        temp=tom
        counter=0
        c=0
        while(tom%2==0):
            counter+=1
            tom=int(tom/2)
        jerry=2**(counter+1)
        if(jerry<=temp):
            c=int(temp/jerry)
        ans.append(c)
    for i in ans:
        print(i)
except:
    pass