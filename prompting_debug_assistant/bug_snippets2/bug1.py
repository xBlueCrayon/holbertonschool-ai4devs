def get_last_items(items, n):
    result = []

    for i in range(len(items) - n, len(items) + 1):
        result.append(items[i])

    return result


numbers = [1, 2, 3, 4, 5]

print(get_last_items(numbers, 2))
