import random
import string

def generate_password(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    all_characters = lower + upper + digits + special

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    print("Generated Password:", generate_password(12))
