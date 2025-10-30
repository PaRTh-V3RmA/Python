# Fibonacci Sequence Generator

def fibonacci(n):
    sequence = [0, 1] 
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]  #

num = int(input("Enter how many Fibonacci numbers you want: "))
fib_seq = fibonacci(num)

print("Fibonacci Sequence:")
print(fib_seq)
