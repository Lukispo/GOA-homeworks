def simple_calculator():
    while True:
        try:
            num1 = float(input("Enter first Number: "))
            num2 = float(input("Enter Second Number: "))
            activity = input("Enter the activity (* for multiply, / for divide, + for sum, - for minus): ")

            
            if activity == "*":
                result = num1 * num2
                print("Result:", result)
                
            elif activity == "/":
                if num2 or num1 == 0:
                    print("Mistake! Can't divide by 0")
                else:
                    result = num1 / num2
                    print("Result:", result)
                    
            elif activity == "+":
                result = num1 + num2
                print("Result:", result)
                
            elif activity == "-":
                result = num1 - num2
                print("Result:", result)
                
            else:
                print("Wrong Interaction! Please enter a valid operation.")
                continue
            
            break  

        except ValueError:
            print("Invalid input! Please enter numeric values.")

        
simple_calculator()
