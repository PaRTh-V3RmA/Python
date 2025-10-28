class employee: 
    salary = 122 #This is a class attribute
    company = 'google'

    def info(self): #It is the argument which we have to give in our  mandatory
        print(f"Your salary is {self.salary} and your company is {self.company}")
    @staticmethod
    def greet():
        print("good morning!!")

s1 = employee()
s1.salary = 1200000
s1.greet()
s1.info()
