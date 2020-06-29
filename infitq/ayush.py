
l1 = list(map(int,input().split(",")))
n = len(l1) 
s = int(input())
count=0
flag=True
for i in range(0,n-3):
    for j in range(i+1,n-2):
        for k in range(j+1,n-1):
            for l in range(k+1,n):
                  if ( (l1[i] + l1[j] + l1[k] + l1[l]) == s): 
                        count+=1
                        flag=False
if(flag):
    print("-1")
else:
    print(count)

  