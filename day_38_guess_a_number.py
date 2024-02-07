# Day 38: Guess a Number

import random

def guess_a_number():
    number = random.randint(1, 10)
    attempts = 0

    while attempts < 3:
        guess = int(input("Guess the number: "))

        if guess > number:
            attempts += 1
            print("Guess is too high")
        elif guess < number:
            attempts += 1
            print("Guess is too low")
        else:
            print("well done, you got gussed the correct number")
        
        if attempts == 3:
            print(f"Wrong!! the number was {number}")

guess_a_number()

# Extra Challenge: Find Missing Numbers

def missing_numbers(num_list):
    missing_numbers = []

    for i in range(1, 32):
        if i not in num_list:
            missing_numbers.append(i)
    
    return missing_numbers

list1 = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]

print(missing_numbers(list1))