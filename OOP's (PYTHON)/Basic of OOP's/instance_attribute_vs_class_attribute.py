class employee: 
    salary = 122 #This is a class attribute
    company = 'google'

s1 = employee()
s1.salary = 120000000000000 #Instance attribute take more prefrence than class attribute
print(s1.salary, s1.company)