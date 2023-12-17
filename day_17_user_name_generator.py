# Day 17, User Name Generator

import random

def user_name():
    name = input("Enter your first name: ")

    rev_name = name[::-1]
    rand_num = random.randint(0,9)

    user = rev_name + str(rand_num)

    print(user)


func_call = user_name()
func_call

# Extra Challenge: Sort by Length

names = ["Peter", "Jon", "Andrew"]

def sort_length(lst_names):
    sorted_names = sorted(lst_names, key=len)

    return sorted_names

func_call_2 = sort_length(names)
print(func_call_2)