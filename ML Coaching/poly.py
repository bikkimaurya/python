class A:
    def m(self):
        print("A")
class B(A):
    def m(self):

        print("b")

obj=B()
obj.m()