def sum_of_list(num_list):
    total = 0
    for num in num_list:
        total += num
    return total
numbers = [10, 20, 30]
result = sum_of_list(numbers)
print("The total sum of the numbers is " + str(result) + ".")
