#  WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted order based on the ram size

class laptop:
    def __init__(self,brand,wasiq,cpu,hdd) -> None:
        self.brand=brand
        self.wasiq=wasiq
        self.cpu=cpu
        self.hdd=hdd

obj1=laptop("Apple",8,'m1','500gb')
obj2=laptop('Lenovo',32,'i5','1tb')
obj3=laptop('HP',16,'i7','1tb')

lis=[]
lis=sorted([obj1.wasiq, obj2.wasiq, obj3.wasiq])
finallist=[]
for i in lis:
    if i==obj1.wasiq:
        finallist.append('obj1')
    elif i==obj2.wasiq:
        finallist.append('obj2')
    else:
        finallist.append('obj3')

print("Final list of object on the basis of there ram : ")
print(finallist)