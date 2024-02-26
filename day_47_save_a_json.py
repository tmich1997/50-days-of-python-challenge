# Day 47: Save a JSON

import json

def save_json(dict_arg):
    file_name = 'names.json'

    with open(file_name, 'w') as json_file:
        json.dump(dict_arg, json_file)

dict_name = {'name': 'Carol', 'sex': 'female', 'age': 55}

save_json(dict_name)

def read_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

        return data
    
print(read_json('names.json'))

