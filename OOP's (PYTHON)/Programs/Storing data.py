class programer:
    company = "Microsoft"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def file(self):
        with open("programers1.txt", 'a') as f:
            f.write(self.name)
            f.write(self.salary)
            f.write(self.company)
            

for i in range(1,4):
    name = input("Enter the name of employee :")
    salary = int(input("Enter the employee salary :"))
    s = str(salary)
    e = programer(name,s)
    e.file()
print("Data has been stored!!!")
#needs improvement