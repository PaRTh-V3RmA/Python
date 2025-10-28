class employee: 
    salary = 122 
    company = 'google'
    def __init__(self,name,salary,company): #those func which are in __'func'__are called dunder method
        self.name = name #even if we not mention in our class it will always initiate
        self.salry = salary
        self.company = company

    def info(self): 
        print(f"Your salary is {self.salary} and your company is {self.company}")

    def greet(self):
        print("Good Morning!!")

s1 = employee("Parth verma", 2000000, "Microsoft") #we have to pass these arguments other wise ------>error
print(f'Your name is {s1.name} and Your current salary is {s1.salry}\nWorking in {s1.company} Company')

#in class if we have to create object blue print by taking some inputs such as name 
#so we can store in it like self.___ = ___ |------> this will store your variable which you passed in 
# __init__