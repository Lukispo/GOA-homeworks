# 1.
def count_letters(text):
    return len(text)  

word = "Hello"
result = count_letters(word)
print("The number of letters in the word is: " + str(result) + ".")

# 2.
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 3.
age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
elif 20 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

#4.
def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return even_numbers, odd_numbers

# Example usage
num_list = [1, 2, 3, 4, 5, 6]
even, odd = separate_even_odd(num_list)
print("Even numbers: " + str(even) + ".")
print("Odd numbers: " + str(odd) + ".")

# 5. Finding Average of a List
def average_of_list(num_list):
    if len(num_list) == 0:
        return 0  
    total = sum(num_list)
    average = total / len(num_list)
    return average

numbers = [10, 20, 30]
result = average_of_list(numbers)
print("The average of the numbers is: " + str(result) + ".")
