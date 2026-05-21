def get_last_items(items, n):
    result = []

    start_index = len(items) - n

    print("Starting index:", start_index)

    for i in range(start_index, len(items)):
        print("Reading index:", i)
        result.append(items[i])

    return result


numbers = [1, 2, 3, 4, 5]

last_items = get_last_items(numbers, 2)

print(last_items)
