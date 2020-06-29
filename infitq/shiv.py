import re
s=input()
special=len(re.findall("[!@#$%^&*(),.?:|<>]",s))
even=re.findall("[02468]",s)
odd=re.findall("[13579]",s)
ans=""

if(special%2==0):
    for i in range(max(len(even),len(odd))):
        if(i<len(even)):
            ans+=str(even[i])
        if(i<len(odd)):
            ans+=str(odd[i])
else:
    for i in range(max(len(even),len(odd))):
        if(i<len(odd)):
            ans+=str(odd[i])
        if(i<len(even)):
            ans+=str(even[i])

print(ans)
        
