# Day 16, Sum the List

def sum_list(nst_lst):
    total = 0

    for row in nst_lst:
        for element in row:
            total += element
    return total


list = [[2, 4, 5, 6], [2, 3, 5, 6]]

func_call = sum_list(list)
print(func_call)

# Extra Challenge: Unpack a Nest

nested_list = [[12, 34, 56, 67], [34, 68, 78]]
new_list = []

for row in nested_list:
    for element in row:
        if element in [34, 67, 78] and element not in new_list:
            new_list.append(element)
print(new_list)
