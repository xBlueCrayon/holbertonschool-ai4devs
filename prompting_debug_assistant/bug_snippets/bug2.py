def divide_numbers(numbers, divisor):
    results = []

    print("Dividing numbers by:", divisor)

    for number in numbers:
        print("Current number:", number)

        result = number / divisor

        results.append(result)

    return results


values = [10, 20, 30]

final_results = divide_numbers(values, 0)

print(final_results)
