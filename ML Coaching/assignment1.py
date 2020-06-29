# 1

i=input("enter to check datatype(Numeric/String) : ")
if(i.isnumeric()):
    print("NUmeric")
else:
    print("String")


# 2

a=list()
b=tuple()
c={}

import re

print(re.findall("'+[a-z]+'",str(type(a))))
print(re.findall("'+[a-z]+'",str(type(b))))
print(re.findall("'+[a-z]+'",str(type(c))))


# 3


def checkDevisiblity(num1,num2):
    if(not(num1%num2)):
        print("devisible")
    else: 
        print("non devisible")


num1= int(input("fist number"))
num2=int(input("input second number"))

checkDevisiblity(num1,num2)



# 4

def maxMin(l):
    minm=l[0]
    maxm=l[0]
    for i in l:
        if(minm>i):
            minm=i
        if(maxm<i):
            maxm=i
    return [minm,maxm]
print(maxMin([1,2,2,0,-12,222]))


# 5

def quebSum(num):
    sum=0
    for i in range(1,num):
        sum+=i**3
    return sum

print(quebSum(int(input("enter a number"))))
