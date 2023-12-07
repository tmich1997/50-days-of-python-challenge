# Day 10, Hide my Password

usr_inp = input("Please enter a password: ")

def hide_password():
    len_str = len(str(usr_inp))
    replace = '*' * len_str
    
    return replace, f"The password is {len_str} characters long"
    

func_call = hide_password()
print(func_call)

# Extra Challenge: A Thousand Seperator

def convert_numbers(inp_list):
    format_num = [format(num, ',') for num in inp_list]
    
    return format_num

lst_num = [1000000, 2356989, 2354672, 9878098]

func_call_2 = convert_numbers(lst_num)
print(func_call_2)