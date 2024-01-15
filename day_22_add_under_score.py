# Day 22, Add Under Score

def add_hash(text_1):
    new_text = '#'.join(text_1)
    return new_text

def add_underscore(text_2):
    new_text = text_2.replace('#', '_')
    return new_text

def remove_underscore(text_3):
    new_text = text_3.replace('_', '')
    return new_text



string_1 = "Python"

func_call = remove_underscore(add_underscore(add_hash(string_1)))
print(func_call)