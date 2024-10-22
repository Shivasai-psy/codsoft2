import random
import string

def password_generator():
    # Prompt user for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 8:
                print("Password length should be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    # Prompt user for password complexity
    print("Choose a password complexity:")
    print("1. Low (only letters)")
    print("2. Medium (letters and numbers)")
    print("3. High (letters, numbers, and special characters)")

    while True:
        complexity = input("Enter the complexity (1/2/3): ")
        if complexity in ['1', '2', '3']:
            break
        else:
            print("Invalid complexity choice! Please choose a valid option.")

    # Generate password based on complexity
    if complexity == '1':
        characters = string.ascii_letters
    elif complexity == '2':
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Display the password
    print(f"Generated Password: {password}")

# Call the password generator function
password_generator()