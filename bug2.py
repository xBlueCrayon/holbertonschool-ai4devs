def divide_numbers(numbers, divisor):
    results = []

    for number in numbers:
        results.append(number / divisor)

    return results


values = [10, 20, 30]

print(divide_numbers(values, 0))
