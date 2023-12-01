# Day 06, User Name Generator

# library for regex
import re

pattern = r'(.*)@'

def user_name(email):
    match = re.match(pattern, email)

    if match:
        user = match.group(1)
        return user

inp_email = 'ben2367@gmail.com'

func_call = user_name(inp_email)
print(func_call)

# Extra Challenge: Zero Both Ends

inp_number = [2, 5, 7, 8, 9]

def zero(lst_number):
    if lst_number:
        lst_number[0] = 0
        lst_number[-1] = 0
    return lst_number

func_call_2 = zero(inp_number)
print(func_call_2)

