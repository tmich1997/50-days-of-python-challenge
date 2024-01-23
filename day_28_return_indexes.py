# Day 28, Return Indexes

def index_positions(str_param):
    indices = []

    for index, char in enumerate(str_param):
        if char.islower():
            indices.append(index)
    
    return indices

s = "LovE"

func_call = index_positions(s)
print(func_call)

# Extra Challenge: Largest Number

def largest_number(arr: list):
    list_1 = []

    n = ''.join(map(str, arr))

    for i in n:
        list_1.append(int(i))
    
    list_1.sort(reverse=True)

    large_number = int(''.join(map(str, list_1)))

    return 'Numebr is {:,}'.format(large_number)

lst = [3, 67, 87, 9, 2]

print(largest_number(lst))