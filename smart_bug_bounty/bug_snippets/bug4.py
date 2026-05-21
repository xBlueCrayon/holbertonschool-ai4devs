def get_last_items(items, n):

    if n <= 0:
        return []

    return items[len(items) - n - 1:]


values = [1, 2, 3, 4, 5]

result = get_last_items(values, 3)

print(result)