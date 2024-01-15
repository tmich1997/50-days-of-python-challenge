# Day 23, Simple Calculator

def simple_calculator():
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    oper_inp = input("What operation would you like to do (+ - / *): ")

    if oper_inp == "+":
        add = first_num + second_num
        return add
    elif oper_inp == "-":
        sub = first_num - second_num
        return sub
    elif oper_inp == "/":
        div = first_num / second_num
        return div
    elif oper_inp == "/" and second_num == 0:
        ZeroDivisionError
    elif oper_inp == "*":
        mult = first_num * second_num
        return mult
    else:
        NameError

func_call = simple_calculator()
print(func_call)

# Extra Challenge: Multiply Words

s = "love live and laugh"
s_1 = "Hate war love Peace"

def multiply_words(arg_string):
    product = 1

    words = arg_string.split()

    for word in words:
        if not any(char.isupper() for char in word):
            product *= len(word)
    return product

func_call_2 = multiply_words(s_1)
print(func_call_2)