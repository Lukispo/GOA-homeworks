def average_of_list(num_list):
    total = sum(num_list)
    average = total / len(num_list) if num_list else 0
    return average
numbers = [10, 20, 30, 40]
result = average_of_list(numbers)
print("The average of the numbers is " + str(result) + ".")
