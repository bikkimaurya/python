left=0
pick=True

maxl=input().split(" ")
maxh=int(maxl[1])

bricks=list(map(int,input().split(" ")))
cmnd=list(map(int,input().split(" ")))
for i in cmnd:
    # left
    if(i==1 and left>0):
        left-=1
    # right
    if(i==2 and left<len(bricks)-1):
        left+=1
    # pick
    if(i==3 and bricks[left]!=0 and pick):
        bricks[left]-=1
        pick=False
        
    # drop
    if(i==4 and bricks[left]<maxh and not(pick)):

        bricks[left]+=1
        pick=True
for brick in bricks:
    print(brick,end=" ")
print()