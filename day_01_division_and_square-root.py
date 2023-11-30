# Day 01, Division and Square-root

def divide_or_square(num):
    if num % 5 == 0:
        return round(num ** 0.5, 2)
    else:
        return num % 5

result = divide_or_square(10)  

print(result)

# Extra Challenge: Longest Value

my_dict = {'fruit': 'apple', 'color': 'green'}

def longest_value(inp_dict):
    max_length = 0
    longest_value = None

    for value in inp_dict.values():
        if len(value) > max_length:
            max_length = len(value)
            longest_value = value

    return longest_value

result_1 = longest_value(my_dict)

print(result_1)
