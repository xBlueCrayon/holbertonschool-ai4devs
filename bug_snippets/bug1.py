def last_n_items(items, n):
    # Return the last n items of a list
    result = []
    length = len(items)
    for i in range(length - n, length):
        result.append(items[i])
    return result  # BUG: fails if n == len(items)

# Test data
numbers = [1, 2, 3, 4, 5]
print("Last 3 items:", last_n_items(numbers, 3))
print("Last 5 items:", last_n_items(numbers, 5))
print("Last 0 items:", last_n_items(numbers, 0))
