class employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class programmer(employee): # if you want that you want to print the constructor of the parent class
    def __init__(self):
        super().__init__() #we use this property of OOPs
        print("Constructor of Programer")
    b = 2
                                                
class manager(programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

p = employee()
o = programmer()
v = manager()

print(p.a)
print(o.a,o.b)
print(v.a,v.b,v.c)