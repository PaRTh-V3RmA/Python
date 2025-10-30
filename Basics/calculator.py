#calculator using basic python
a=int(input("Enter the first number : "))
operator = str(input("Enter the operator(+,-,*,/) : "))
b=int(input("Enter the second numebr :"))

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divison(a,b):
    return a/b

if operator=='+':
    print(add(a,b))
elif operator=='-':
    print(sub(a,b))
elif operator=='*':
    print(multiply(a,b))
elif operator=='/':
    print(divison(a,b))
else:
    print("invalid operator!!")

#simplest form of the calculator(mediocre)
def cal():
    user_input = eval(input("Enter the calculation-->"))
    return user_input
print(cal())