# Day 02, Strings to Integers

def convert_add(inp_lst):
    return sum(int(i) for i in inp_lst)

lst = ["1", "3", "5"]

func_call = convert_add(lst)

print(func_call)

# Extra Challenge: Duplciate Names

def check_duplicates(lst_dup):
    seen = set()
    duplicates = set()

    for item in lst_dup:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    if duplicates:
        return list(duplicates)
    else:
        return "No duplicates"

lst_2 = ['apple', 'orange', 'peach', 'orange', 'apple']

func_call_2 = check_duplicates(lst_2)
print(func_call_2)