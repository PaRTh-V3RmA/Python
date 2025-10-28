num = int(input("Enter the number :"))
def perfect(num):
    list_divisors = []
    sum = 0
    for i in range(1,num+1):
        if num%i==0:
            list_divisors.append(i)
        else:
            pass
    for z in range(len(list_divisors)):
        if z<len(list_divisors)-1:
            sum+=list_divisors[z]
    if sum == num:
        print(num, 'it is a perfect number')
    else:
        print(num,"it is not a perfect number")
perfect(num)