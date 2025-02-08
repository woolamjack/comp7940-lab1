def print_factor():
    x = int(input("Enter a number to find its factors: "))  # Get user input
    factors = []
    for i in range(1, x + 1):  # Start from 1 to x
        if x % i == 0:  # Check if i is a factor of x
            factors.append(i)
    print(f"Factors of {x}: {factors}")

# Call the function
print_factor()