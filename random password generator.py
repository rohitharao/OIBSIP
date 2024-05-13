import secrets
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_symbols=True, use_lowercase=True):
    lowercase = string.ascii_lowercase if use_lowercase else ""
    uppercase= string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""

    all_characters = lowercase + uppercase + numbers + symbols

    if not all_characters:
        raise ValueError("At least one character set must be enabled")

    return ''.join(secrets.choice(all_characters) for _ in range(length))

try:
    length = int(input("Enter password length (6-14): "))
    if length < 6 or length > 14:
        raise ValueError("Password length must be between 6 and 14")

    use_uppercase = bool(input("Use uppercase letters (y/n): ").lower() == "y")
    use_numbers = bool(input("Use numbers (y/n): ").lower() == "y")
    use_symbols = bool(input("Use symbols (y/n): ").lower() == "y")
    use_lowercase = bool(input("Use lowercase letters (y/n): ").lower() == "y")

    if not (use_uppercase or use_numbers or use_symbols or use_lowercase):
        print("At least one character set must be enabled as yes.")

    else:
        password = generate_password(length, use_uppercase, use_numbers, use_symbols, use_lowercase)
        print(f"Generated password: {password}")

except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"An error occurred: {e}")