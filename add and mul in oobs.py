class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def addition(self):
        return self.num1+self.num2
    def mul(self):
        return self.num1*self.num2
    

obj1=calculator(10,20)
print("Addition is",obj1.addition())
print("Multiplication is",obj1.mul())


obj2=calculator(100,200)
print("Addition is",obj2.addition())
print("Multiplication is",obj2.mul())
