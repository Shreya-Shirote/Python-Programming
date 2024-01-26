import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one type of character (letters, numbers, or symbols).")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    # Add your own criteria for password strength here
    # For example, you can check for minimum length, the presence of uppercase/lowercase letters, etc.
    return len(password) >= 8

def main():
    print("Password Generator")

    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        length = int(input("Enter the desired length of the password: "))
        use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

        passwords = []

        for _ in range(num_passwords):
            password = generate_password(length, use_letters, use_numbers, use_symbols)

            if password:
                print(f"Generated Password: {password}")
                if check_password_strength(password):
                    print("Password Strength: Strong")
                else:
                    print("Password Strength: Weak (Consider increasing length or including more character types)")
                passwords.append(password)

        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, 1):
            print(f"{i}. {password}")

    except ValueError:
        print("Error: Please enter valid inputs.")

if __name__ == "__main__":
    main()
