class Myclass:
    def __init__(self,value):
        self.value=value
    @classmethod
    def classMethod(cls,value):
        method=cls(value)
        return method
obj=Myclass.classMethod(50)
print(obj.value)
        
