class employee: 
    company = "Google"
    salary = 1000000
    def show(self,name):
        self.name = name
        print(f"The name is {self.name} and the salary is {self.salary}")
        return name

class coder:
    language = 'Python'
    def printlanguages(self):
        print(f"Your language is {self.language}")

class programer(employee,coder): #In this case the child has two parent means we can use multiple classes in in one class
    company = 'Google company'

s1 = programer() 
s1.show('Parth verma')
s1.printlanguages()

