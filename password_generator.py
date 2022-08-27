import random
import string

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = string.punctuation.replace("-", "")


def generator(**kwargs):
    length = kwargs.get("length", 14)
    characters = get_characters(**kwargs)

    password = ""
    for i in range(length):
        if i % 4 == 0 and i != 0 and i + 1 != length:
            password += "-"
        else:
            password += random.choice(characters)
            
    return password
def get_characters(**kwargs):
    uppercase = kwargs.get("uppercase")
    lowercase = kwargs.get("lowercase")
    digits = kwargs.get("digits")
    symbols = kwargs.get("symbols")

    characters = ""
    if uppercase:
        characters += UPPERCASE
    if lowercase:
        characters += LOWERCASE
    if digits:
        characters += DIGITS
    if symbols:
        characters += SYMBOLS

    if len(characters) == 0:
        return UPPERCASE + LOWERCASE + DIGITS + SYMBOLS

    return characters
