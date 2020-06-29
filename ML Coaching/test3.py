import pickle
with open("./text.py","wb") as file:
    pickle.dump( ["101 abhishek bhopla 2000","102 abeishek bla 4000"],file)

emp={}
with open("./text.py","rb") as file:
    print(pickle.load(file))
    



