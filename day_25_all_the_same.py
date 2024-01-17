# Day 25, All the Same

def all_the_same(arg):
    if isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, str):
        if all(element == arg_list[0] for element in arg):
            return True
        else:
            return False
    else:
        TypeError, "Input must be a string, a list, or a tuple."

arg_list = ["Mary", "Mary", "Mary"]

func_call = all_the_same(arg_list)
print(func_call)

# Extra Challenge: Reverse a String

str1 = "the love is real"

def read_backwards(str_arg):
    str_back = str_arg.split()
    reversed_str = ' '.join(reversed(str_back))

    return reversed_str

func_call_2 = read_backwards(str1)
print(func_call_2)
