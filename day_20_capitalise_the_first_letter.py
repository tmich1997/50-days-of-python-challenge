# Day 20, Word and Elements

def capitalise(arg_string):
    return arg_string.title()

string = "i like learning"

func_call = capitalise(string)
print(func_call)

# Extra Challenge: Reversed List

str1 = 'leArning is hard, bUt if You appLy youRself you can achieVe success'

def contains_capital(string):
    words = string.split()

    word_list = []

    for word in words:
        if any(char.isupper() for char in word):
            word_list.append(word[::-1])
    return word_list 

print(contains_capital(str1))