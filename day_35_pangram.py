# Day 35: Pangram

import string

alpha = set(string.ascii_lowercase)

def check_panagram(str):
    return set(str) >= alpha

sent = 'the quick brown fox jumps over a lazy dog'

print(check_panagram(sent))

# Extra Challenge: Find my Position

def find_index(lst_int, num):

    if num in lst_int:
        index_pos = [index for index, value in enumerate(lst_int) if value == num]
        
        return index_pos
    else:
        return [num] * len(lst_int)

list_1 = [1, 2, 4, 6, 7, 7]

print(find_index(list_1, 8))