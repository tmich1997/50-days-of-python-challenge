# Day 30, Most Repeated Name

def repeated_name(lst_names):
    name_counts = {}

    for name in lst_names:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

    most_repeated_name = max(name_counts, key=name_counts.get)
    count = name_counts[most_repeated_name]

    return most_repeated_name, count

name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]

func_call = repeated_name(name)
print(func_call)


# Extra Challenge: Sort by Last Name

def sort_and_swap(names):
    sorted_names = sorted(names, key=lambda x: x.split()[-1])
    swapped_names = [" ".join(reversed(name.split())) for name in sorted_names]
    return swapped_names

names = ["Beyoncé Knowles", "Alicia Keys", "Katie Perry", "Chris Brown", "Tom Cruise"]

result = sort_and_swap(names)
print(result)
        

