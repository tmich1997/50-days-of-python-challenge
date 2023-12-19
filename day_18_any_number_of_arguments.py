# Day 18, Any Number of Arguments

from statistics import mean

def any_number(*args):
    return mean(args)

func_call = any_number(12, 90)
print(func_call)

# Extra Challenge: Add and Reverse

def add_reverse(lst_1, lst_2):
    result = []

    for i, j in zip(lst_1, lst_2):
        result.append(i + j)
    
    return result[::-1]

list_1 = [10, 12, 34]
list_2 = [12, 56, 78]

func_call_2 = add_reverse(list_1, list_2)
print(func_call_2)

