# Day 33, List Intersection

def inter_section(lst_a, lst_b):
    intersect_list = []

    for element in lst_a:
        if element in lst_b:
            intersect_list.append(element)
    
    intersect_list.reverse()
    return intersect_list

list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]

func_call = inter_section(list1, list2)
print(func_call)

# Extra Challenge: Set or List

import timeit

set_search = '''
a = range(10000000)
b = set(a)
i = 999999
i in b
'''

set_search_time = timeit.timeit(stmt=set_search, number=1000)
print(set_search_time)

list_search = '''
a = range(10000000)
b = list(a)
i = 999999
i in b
'''

list_search_time = timeit.timeit(stmt=list_search, number=1000)
print(list_search_time)