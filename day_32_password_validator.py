# Day 32, Password Validator

def passsword_validator():
    while True:
        inp_password = input("Enter a password: ")
        
        if not any(char.isupper() for char in inp_password):
            print("Must contain at least one uppercase letter.") 
        elif not any(char.islower() for char in inp_password):
             print("Must contain at least one lowercase letter.") 
        elif not any(char.isdigit() for char in inp_password):
            print("Must contain at least one digit.")
        elif len(inp_password) < 8:
            print("Must be at least 8 characters long.")
        elif any(char.isupper() for char in inp_password) and any(char.islower() for char in inp_password) and any(char.isdigit() for char in inp_password) and len(inp_password):
            print(inp_password)
            break
        else:
            print("enter a passwrd")

passsword_validator()

# Extra Challenge: Valid Email

emails = ["ben@mail.com", "john@mail.cm", "kenny@gmail.com", "@list.com"]

def email_validator(lst_emails):
    for email in lst_emails:
        if email.count("@") == 1:
            left = email.split("@")[0]
            if len(left) > 0 and ".com" in email:
                print(email)


email_validator(emails)