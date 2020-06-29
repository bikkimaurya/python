
def maxMin(l):
    minm=l[0]
    maxm=l[0]
    for i in l:
        if(minm>i):
            minm=i
        if(maxm<i):
            maxm=i
    return [minm,maxm]


