# Day 07, A String Range

def string_range(num):
    list = []
    for i in range(num):
        list.append(str(i) + ".")
    
    return list

func_call = string_range(6)
print('"' + "".join(func_call) + '"')

# Extra Challenge: Dictionary of Names

names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

def dictionary_of_names(lst_names):
    result_dict = {}

    for name in lst_names:
        if name.startswith('S'):
            if name in result_dict:
                result_dict[name] += 1
            else:
                result_dict[name] = 1
        
    return result_dict
        
func_call_2 = dictionary_of_names(names)
print(func_call_2)