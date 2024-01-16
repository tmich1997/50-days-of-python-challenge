# Day 24, Average Calories

def average_calories():
    cal_intake = int(input("What was your calorie intake:"))
    duration = int(input("For how many days? "))

    avg_cal = round(cal_intake/duration, 2)

    return f'Your avergae calorie intake across {duration} days was {avg_cal} calories'

func_call = average_calories()
print(func_call)

# Extra Challenge: Create a Nested List

def nested_list(nst_list):
    new_lst = []

    for i in nst_list:
        if isinstance(i, list):
            new_lst.append(i)
        else:
            return "Invalid arguments. Please check your arguments."
    
    return new_lst

nest_list = [1, 2, 3, 5], [1, 2, 3, 4], [1,3, 4, 5]
nest_list_2 = (1, 2, 3, 5), [1, 2, 3, 4], [1,3, 4, 5]

func_call_2 = nested_list(nest_list)
print(func_call_2)