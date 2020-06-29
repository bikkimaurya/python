q=int(input())
for _ in range(q):
    n=int(input())
    if(n%2==1):
        print(int((n-1)/2))
    else:
        while(n and (not(n&1)) ):
            n=n>>1
        n=n>>1
        print(n)