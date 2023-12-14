# Day 15, Same in Reverse

def same_in_reverse(str):
    if str == str[::-1]:
        return True
    else:
        return False

inp_string = "timble"

func_call = same_in_reverse(inp_string)
print(func_call)

# Extra Challenge: Whats my Age

names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}

def your_age():
    global names_age

    inp_name = input("Please enter your name: ").lower()

    for key in names_age.keys():
        if key == inp_name:
            print(f"{inp_name.title()}, you are {names_age[inp_name.lower()]} years old.")
    else:
        while inp_name not in names_age.keys(): 
            inp_age = input("Your name is not in the dictionary, please enter your age: ").lower()

            names_age.update({inp_name: inp_age})
            print(f"Hi, {inp_name.title()}! you are {inp_age} years old.")

your_age()
print(names_age)