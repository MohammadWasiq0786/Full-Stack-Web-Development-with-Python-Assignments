# Write a python script to add the new method in SmartPhone class which accepts
# Truecaller object as a parameter and call the fetch method of Truecaller

class truecaller:

    def __init__(self) -> None:
        self.data={'9876543210':"Ram",'9988776655':"Shyam","9878767890":"Asteek"}

    def add_data(self,key,value):
        self.data[key]=value

    def fetch(self,key):
        return self.data[key]

class smartphone():
    
    def accept_input(self,tc,num):
       return tc.fetch(num)


tc_obj=truecaller()
sp_obj=smartphone()

print(sp_obj.accept_input(tc_obj,'9876543210'))

