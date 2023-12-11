# Day 12, Count the Dots

def count_dots(str):
    count = 0

    for dot in str:
        if dot == ".":
            count += 1
    return count

string = "he.l.p"

func_call = count_dots(string)
print(func_call)

# Extra Challenge: Your Age in Minutes

from datetime import datetime

def age_in_minutes():
    while True:
        try:
            dob_input = int(input("Enter your date of birth: "))
           
            if 1900 <= dob_input <= datetime.now().year:
                years = datetime.now().year - dob_input
                minutes_in_year = 60 * 24 * 365
                return f"You are {format(years * minutes_in_year, ',')} minutes old."
            else:
                print("Invalid input. Please enter a valid 4-digit year between 1900 and the current year.")
        except ValueError:
            print("Invalid input. Please enter a valid 4-digit year.")

func_call_2 = age_in_minutes()
print(func_call_2)
