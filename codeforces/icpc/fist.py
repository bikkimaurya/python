a=open("/home/bikki__maurya/Coding/VSCode/Python/codeforces/icpc/1.txt")
data=a.read()
l=list(map(int,data.split(" ")))
l.sort()
a=open("/home/bikki__maurya/Coding/VSCode/Python/codeforces/icpc/2.txt","w")
s=str(l)
s=s.replace(",", "")
s=s.replace("[","")
s=s.replace("]","")
a.write(s)