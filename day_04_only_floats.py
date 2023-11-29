# Day 04, Only Floats

def only_floats(a,b):
    if isinstance(a, float) and isinstance(b, float):
        return 2
    elif isinstance(a, float) or isinstance(b, float):
        return 1
    else:
        return 0

func_call = only_floats(12, 12)

print(func_call)

# Extra Challenge: Index of the Longest Word 

def word_index(word_list):
    longest_word = word_list[0]

    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    
    index = word_list.index(longest_word)
    return index


words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]

func_call_2 = word_index(words1)
print(func_call_2)
