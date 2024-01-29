# Day 31, Longest Words

def longest_word(lst_words):
    longest = ""
    max_length = 0

    for word in lst_words:
        if len(word) > max_length:
            longest = word
            max_length = len(word)
    
    return [max_length, longest]
        

list = ['Java', 'JavaScript', 'Python']

func_call = longest_word(list)
print(func_call)

# Extra Challenge: Create User

def create_user():
    user_dict = {}

    inp_name = input("Enter your name: ")
    inp_age = int(input("Enter your age: "))
    inp_password = input("Enter your password: ")

    user_dict['name'] = inp_name
    user_dict['age'] = inp_age
    user_dict['password'] = inp_password

    print("User Saved. Please login.")

    while True:
        user_name = input("Enter your name: ")
        user_password = input("Enter your password: ")

        if user_name == user_dict['name'] and user_password == user_dict['password']:
            print("Logged in successfully")
            break
        else:
            print("Wrong password or user name, please try again")

create_user()

