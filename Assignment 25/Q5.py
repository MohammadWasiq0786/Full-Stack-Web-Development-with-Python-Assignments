# Write a python script to create a Calculator class with 2 methods for adding and subtracting 2 values

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
    
obj=Calculator()
obj.setdata(7,5)
print("Adding : ",obj.adding())
print("Subtracting : ",obj.subtracting())