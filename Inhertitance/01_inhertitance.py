class employee: #This is Parent class 
    company = "Google"
    salary = 1000000
    def show(self,name):
        self.name = name
        print(f"The name is {self.name} and the salary is {self.salary}")
        return name

class programer(employee): #This is Derived class or we can say this is Child class of parent class
    company = 'Google company'
    @staticmethod
    def showlang():
        print("Your language is Python")

s1 = programer() #We use the child class to call the Parent class
s1.show('Parth verma')
s1.showlang()

#We can reproduce multiple childs as biology !!