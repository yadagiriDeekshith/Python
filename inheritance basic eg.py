class A:
    def display(self):
        print("Deekshith")
class C:
    def show(self):
        print("Yadagiri")
class D:
    def non(self):
        print("Chowdary")
class B(C,A,D):
    pass
obj=B()
obj.show()
obj.display()
obj.non()
