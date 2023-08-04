import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_numbers=True, include_special_chars=True):
    chars = ""
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_numbers:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation

    if not chars:
        print("Error: No character set selected.")
        return None

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Password Length: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    generated_password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)
    if generated_password:
        print("Generated Password:", generated_password)
