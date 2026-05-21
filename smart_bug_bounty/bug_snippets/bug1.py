def calculate_average(numbers):

    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)

    return average


data = []

result = calculate_average(data)

print("Average:", result)
