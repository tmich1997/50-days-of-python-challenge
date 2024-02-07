# Day 39: Password Generator

import random
import string

def generate_password():
    char  = string.ascii_letters + string.digits + string.punctuation

    pass_strength = input("How strong do you want your password to be (weak, strong, very strong): ")

    if pass_strength == "weak":
        random_string = ''.join(random.choice(char) for i in range(5))
        return random_string
    elif pass_strength == "strong":
        random_string = ''.join(random.choice(char) for i in range(8))
        return random_string
    elif pass_strength == "very strong":
        random_string = ''.join(random.choice(char) for i in range(12))
        return random_string

print(generate_password())