a=[]
for i in range(int(input())):
    a.append(int(input()))
a.sort()

maxm=a[0]*len(a)
for i in range(1,len(a)):
    temp=a[i]*len(a[i:])
    if(temp>maxm):
        maxm=temp
print(maxm)
