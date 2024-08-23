password = input("Please enter your password: ") # First Password!
password_confirm = input("Please confirm your password: ") # Confirmation of the first password

while password != password_confirm: # Checking if User made mistake
    password_confirm = input("Wrong Password. Try again: ") # If they did they get another chance :D
else:
    print("Password remembered!") # If anything else happens it prints this
