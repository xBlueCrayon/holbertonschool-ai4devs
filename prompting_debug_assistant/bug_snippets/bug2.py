def divide_numbers(a, b):
    # Divide a by b
    return a / b  # BUG: division by zero not handled

# Test cases
print(divide_numbers(10, 2))
print(divide_numbers(10, 0))  # triggers exception
print(divide_numbers(5, 5))
