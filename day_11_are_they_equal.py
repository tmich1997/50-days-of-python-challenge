# Day 11, Are They Equal?

def equal_strings(str_1, str_2):
    if all(char in str_2 for char in str_1) and all(char in str_1 for char in str_2):
        return True
    else:
        return False

string_1 = "love"
string_2 = "lods"

func_call = equal_strings(string_1, string_2)
print(func_call)

# Extra Challenge: Swap Values

def swap_values(lst_number):
    first_num = lst_number[-1]
    last_num = lst_number[0]

    lst_number[0] = first_num
    lst_number[-1] = last_num

    return lst_number

list = [2, 4, 67, 7]

func_call_2 = swap_values(list)
print(func_call_2)
