# Day 26, Sort Words

def sort_words(str_arg):
    seen = set()
    wrd_list = []

    for word in str_arg:
        if word != ' ' and word not in seen:
            wrd_list.append(word)
            seen.add(word)
    return wrd_list

s = "love life"

func_call = sort_words(s)
print(func_call)

# Extra Challenge: Length of Words

def string_length(lgnt_arg):
    length_dict = {}

    word_list = lgnt_arg.split()

    for item in word_list:
        length = len(item)
        length_dict[item] = length

    return length_dict

s = 'Hi my name is Richard'

func_call_2  = string_length(s)
print(func_call_2)