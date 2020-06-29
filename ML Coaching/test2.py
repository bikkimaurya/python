with open("./text.py","w") as file:
    # file.write("print('hello world')")
    file.writelines([ x+"\n" for x in ["101 abhishek bhopla 2000","102 abeishek bla 4000"]])
    # print(file.readlines())
    # file.seek() #to move the pointer 
    # file.tell() #to find cursor position



emp={}
with open("./text.py","r") as file:
    for data in file.readlines():
        abcd=data.split(" ")
        print(len(abcd))
        if(len(abcd)>3):
            emp[abcd[0]]=[abcd[1],abcd[2],abcd[3]]
print(emp)



