numbers = list(range(1, 11))
print("Original Numbers:", numbers)

first_half = numbers[:5]
print("First Half:", first_half)

second_half = numbers[5:]
print("Second Half:", second_half)

squares = [x**2 for x in numbers]
print("Squares:", squares)
