n = int(input("Enter the number: "))

def binomial(n):
    triangle = [[1]]
    # Generate subsequent rows
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1

        # Calculate middle elements
        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j + 1])

        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)
    
    print(triangle[-1])

binomial(n)
