nk=input().split(" ")
k=int(nk[1])
count=0
l=list(map(int,input().split()))
for i in range(len(l)-1):
    if(abs(l[i]-l[i+1])>=k):
        count+=1
print(count)