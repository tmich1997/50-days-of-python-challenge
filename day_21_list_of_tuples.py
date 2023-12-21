# Day 21, Word and Elements

def make_tuples(lst_1, lst_2):
    if len(lst_1) == len(lst_2):
        return list(zip(lst_1, lst_2))
    else:
        ValueError

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]

func_call = make_tuples(list_1, list_2)
print(func_call)

# Extra Challenge: Even Number or Average

def even_or_average():
    largest_even = None

    user_inp_1 = int(input("Enter a number: "))
    user_inp_2 = int(input("Enter a number: "))
    user_inp_3 = int(input("Enter a number: "))
    user_inp_4 = int(input("Enter a number: "))
    user_inp_5 = int(input("Enter a number: "))

    num_list = []

    num_list.append(user_inp_1)
    num_list.append(user_inp_2)
    num_list.append(user_inp_3)
    num_list.append(user_inp_4)
    num_list.append(user_inp_5)

    for num in num_list:
        if num % 2 == 0:
            if largest_even is None or num > largest_even:
                largest_even = num
    if largest_even is not None:
        return largest_even
    else:
        return sum(num_list)/len(num_list)

    
func_call_2 = even_or_average()
print(func_call_2)