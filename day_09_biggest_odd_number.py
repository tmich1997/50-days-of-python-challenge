# Day 09, Biggest Odd Number

# Method 1
def biggest_odd(str_num):
    for i in str_num:
        if int(i)%2 != 0:
            big_odd = max(i)
    return big_odd

num = "23569"

func_call = biggest_odd(num)
print(func_call)

# Method 2 (using list comprehension)
def biggest_odd_2(str_num_2):
    odd_digits = [int(digit) for digit in str_num_2 if int(digit)%2 != 0]
    if odd_digits:
        return max(odd_digits)

num_2 = "23569"

func_call_2 = biggest_odd_2(num_2)
print(func_call_2)

# Extra Challenge: Zeros to the End

def zeros_last(lst_num):
    non_zero = [num for num in lst_num if num != 0]
    zeros = [num for num in lst_num if num == 0]
    return non_zero + zeros

number_lst = [1, 4, 6, 0, 0, 7, 0, 9]

func_call_3 = zeros_last(number_lst)
print(func_call_3)