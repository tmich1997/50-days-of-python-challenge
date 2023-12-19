# Day 19, Word and Elements

def count_words(word_count):
    words = word_count.split()
    num_word = len(words)

    return(num_word)

def count_elements(element_count):
    num_characters = len([char for char in element_count if char.isalnum()])

    return num_characters

string_word = "I love learning,"

func_call = count_words(string_word)
print(func_call)

func_call_2 = count_elements(string_word)
print(func_call_2)
