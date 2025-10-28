class employee:
    a = 1

class programmer(employee):
    b = 2

class manager(programmer):
    c = 3

p = manager()
print(p.a)
print(p.b)
print(p.c)

# in this case parent class have two child class and the smallest child is manager()