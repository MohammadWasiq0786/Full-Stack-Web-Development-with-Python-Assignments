#  Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
# and division of 2 values and inherit it from the Calculator class

class Calculator:

    def __init__(self) -> None:
        self.x=None
        self.y=None
    
    def setdata(self, x, y):
        self.x=x
        self.y=y
    
    def adding(self):
        return self.x+self.y
    
    def subtracting(self):
        return self.x-self.y

class Calculator2(Calculator):
    def multiplication(self):
        return self.x*self.y

    def division(self):
        return self.x/self.y

obj=Calculator2()
obj.setdata(7,5)
print("Adding : ",obj.adding())
print("Subtracting : ",obj.subtracting())
print("Multiplication : ",obj.multiplication())
print("Division : ",obj.division())