print("Think of a number between 1 and 100.")
input("Press Enter when you're ready...")

low = 1
high = 100
number = int(input("Enter the number you thought of (1-100): "))

while True:
    guess = (low + high) // 2
    print("My guess is " + str(guess) + ".")
    
    if guess == number:
        print("Yay! I guessed your number correctly, it is " + str(guess) + "!")
        break
    elif guess < number:
        low = guess + 1
    else:
        high = guess - 1