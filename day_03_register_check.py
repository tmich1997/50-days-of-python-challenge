# Day 03, Register Checks

def register_check(my_dict):
    count = 0

    for key, value in my_dict.items():
        if value == 'yes':
            count += 1
    return count

inp_dict = {
    'Michael': 'yes',
    'John': 'no',
    'Peter': 'yes',
    'Mary': 'yes'

}

call_func = register_check(inp_dict)

print(call_func)

# Extra Challenge: Lowercase Names

def lowercase_nanes(inp_names):
    for i in inp_names:
        if i.islower():
            print(i)

names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

call_func_2 = lowercase_nanes(names)

call_func_2