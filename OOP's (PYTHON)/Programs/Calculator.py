class calculator :
    print("Calculator")
    def __init__(self,number):
        self.num = number
        self.square(number)
        self.square_root(number)
        self.cube(number)
        
    @staticmethod
    def hello():
        print("Hello")

    def square(self,num):
        num = num**2
        print(num)
        return num
    
    def square_root(self,num):
        num = num**(1/2)
        print(num)
        return num
    
    def cube(self,num):
        num= num**3
        print(num)
        return num

number = int(input("Enter the number : "))
n1 = calculator(number)
n1.hello()

