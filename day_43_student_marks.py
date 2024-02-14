# Day 43: Student Marks

import string

def student_marks():
    student_dict = {}

    while True:
        try:
            input_name = input("Enter the students name: ")
            for letter in input_name:
                if letter in string.punctuation or letter in string.digits:
                    raise NameError("Please enter a valid name")
                
            if input_name == 'done':
                break


            input_marks = int(input("Enter the students marks: "))

            student_dict[input_name] = input_marks
        except (NameError, ValueError) as e:
            print(f"Error: {e}")

    return student_dict


print(student_marks())

