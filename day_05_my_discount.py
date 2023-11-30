# Day 05, My Discounts

full_price = int(input("Enter the full price: "))
discount = int(input("Enter the discount amount as a whole number: "))

def my_discount():
    discounted_price = full_price - (full_price * (discount/100))
    return "The discounted price is " + "$"+ str(round(discounted_price,2))

call_function = my_discount()
print(call_function)

# Extra Challenge: Tuple of Student Sex

students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male',
'female']

def number_of_students(inp_list):
    male_count = 0
    female_count = 0

    for i in inp_list:
        if i.lower() == 'male':
            male_count += 1
        elif i.lower() == 'female':
            female_count += 1
    return [("Male", male_count), ("female", female_count)]

call_function_2 = number_of_students(students)
print(call_function_2)