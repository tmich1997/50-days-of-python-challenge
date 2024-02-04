# Day 36: Count String

def count_letters(str_arg):
    count_dict = {}

    for char in str_arg:
        if char.isalpha():
            char_lower = char.lower()  # Convert to lowercase to make it case-insensitive
            count_dict[char_lower] = count_dict.get(char_lower, 0) + 1

    return count_dict

string = 'hello'
result_dict = count_letters(string)
print(result_dict)

# Extra Challenge: Sum a Nested Dictionary

def sum_nested_dict(nst_dict):
    total_sum = 0
    for value in nst_dict.values():
        if isinstance(value, dict):
            total_sum += sum_nested_dict(value)
        else:
            total_sum += value
    return total_sum

nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}, 'g': 5}

total_sum = sum_nested_dict(nested_dict)
print(total_sum)