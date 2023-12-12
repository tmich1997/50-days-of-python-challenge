# Day 14, Flatten the List

def flat_list(lst):
    lst_flat = []
    for row in lst:
        lst_flat.extend(row)
    return lst_flat

list = [[2, 4, 5, 6]]

func_call = flat_list(list)
print(func_call)

# Extra Challenge: Teachers Salary

def your_salary():
    inp_name = input("Enter your name: ")
    inp_periods = int(input("Enter the number of periods: "))
    int(input("Enter your rate per period: "))

    monthly_rate = 20
    overtime_rate = 25
    overtime_threshold = 100

    if inp_periods > 100:
        overtime_diff = inp_periods - 100
        monthly_salary = (overtime_diff * overtime_rate) + (overtime_threshold * monthly_rate)
        
        print(f"Teacher: {inp_name}")
        print(f"Periods: {inp_periods}")
        print(f"Gross salary: {monthly_salary}")
    else:
        monthly_salary = inp_periods * monthly_rate

        print(f"Teacher: {inp_name}")
        print(f"Periods: {inp_periods}")
        print(f"Gross salary: ${monthly_salary}")
        
func_call_2 = your_salary()
func_call_2