ans=0

for q in range(int(input())):
    ans=0
    n=int(input())
    string=list(map(int,input().split(" ")))
    for i in range(0,len(string)-1):
        a=abs(string[i]-string[i+1])
        if(a>0):
            a=a-1
            ans+=a
    print(ans)
