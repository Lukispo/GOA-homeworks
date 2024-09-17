list = list(range(1, 11))
first_half = list[:5]
second_half = list[5:]
squares = [num ** 2 for num in list]
print(squares, second_half, first_half)