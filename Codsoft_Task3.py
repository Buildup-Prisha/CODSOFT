import random
import string

def generate_password(length, use_digits=True, use_symbols=True):
    # Base character set: lowercase + uppercase letters
    characters = string.ascii_letters  # a-z + A-Z

    if use_digits:
        characters += string.digits  # 0-9

    if use_symbols:
        characters += string.punctuation  # !@#$%^&* etc.

    # Ensure at least one character is used
    if length < 3:
        return "Password length must be at least 3"

    # Randomly generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        
        # Ask user whether to include digits and symbols
        include_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
        include_symbols = input("Include special characters? (y/n): ").strip().lower() == 'y'

        # Generate the password
        password = generate_password(length, use_digits=include_digits, use_symbols=include_symbols)

        print(f"\n Generated Password: {password}")

    except ValueError:
        print(" Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
