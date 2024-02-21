# Day 45: Words & Special Characters

import re

def analyse_string(str_arg):
    my_dict = {
        "special_character": 0,
        "numeric_character": 0,
        "total_character": 0
    }

    special_character_pattern =  r'[#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]'
    numeric_character_pattern = r'\d'
    total_character_pattern = r'\S'

    special_character_find = re.findall(special_character_pattern, str_arg)
    numeric_character_find = re.findall(numeric_character_pattern, str_arg)
    total_character_find = re.findall(total_character_pattern, str_arg)

   
    my_dict['special_character'] = len(special_character_find)
    my_dict['numeric_character'] = len(numeric_character_find)
    my_dict['total_character'] = len(total_character_find)


    print(my_dict)


string = '"Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%seggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".'

analyse_string(string)
