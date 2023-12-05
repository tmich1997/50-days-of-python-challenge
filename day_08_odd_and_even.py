# Day 08, Odd and Even

def odd_even(lst_numbers):
    max_num = lst_numbers[0]
    min_num = lst_numbers[0]

    for i in lst_numbers:
        if i%2 == 0 and i > max_num:
            max_num = i
        elif i%2 != 0 and i < min_num:
            min_num = i
    return max_num - min_num

numbers = [1, 2, 4, 6]

func_call = odd_even(numbers)
print(func_call)

# Extra Challenge: List of Prime Numbers

input_number = int(input("Please enter a number greater than 2: "))

def prime_numbers(inp_number):
    if inp_number < 2:
        return False

    for i in range(2, int(inp_number**0.5) +1):
        if inp_number % i == 0:
            return False
    
    return True

for num in range(2, input_number + 1):
    if prime_numbers(num):
        print(num)