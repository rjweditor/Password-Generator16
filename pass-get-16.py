import random
import string

def generate_password():
    # Define character sets for lowercase letters, uppercase letters, special characters, and numbers
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    special_chars = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"
    numeric_chars = string.digits

    # Initialize an empty password
    password = []

    # Choose at least one character from each character set
    password.append(random.choice(lowercase_chars))
    password.append(random.choice(uppercase_chars))
    password.append(random.choice(special_chars))
    password.append(random.choice(numeric_chars))

    # Generate the remaining characters
    remaining_length = 16 - len(password)
    all_chars = lowercase_chars + uppercase_chars + special_chars + numeric_chars
    password.extend(random.choices(all_chars, k=remaining_length))

    # Shuffle the characters to randomize the password
    random.shuffle(password)

    # Convert the list of characters to a string
    password_str = ''.join(password)

    return password_str

# Generate and print a random password
random_password = generate_password()
print("Random Password:", random_password)
