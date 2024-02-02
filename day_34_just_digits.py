# Day 34, Just Digits

import csv

def just_digits():
    with open("python.csv", 'r') as f:
        f_csv = csv.reader(f)

        num_list = []

        for row in f_csv:
            for item in row:
                current_num = ''
                for char in item:
                    if char.isdigit():
                        current_num += char
                    elif current_num:
                        num_list.append(current_num)
                        current_num = ''
                
                if current_num:
                    num_list.append(current_num)

        print(num_list)

    

just_digits()