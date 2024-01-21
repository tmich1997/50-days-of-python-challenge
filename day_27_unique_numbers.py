# Day 26, Unique Numbers

def unique_numbers(num_list):
   all_num_sum = sum(num_list)
   uniq_num_sum = sum(set(num_list))

   if (all_num_sum - uniq_num_sum) % 2 == 0:
      return num_list
   else:
      list(set(num_list))
      
lst = [1, 2, 4, 5, 6, 7, 8, 8]

func_call = unique_numbers(lst)
print(func_call)

# Extra Challenge: Difference of Two Lists

def difference(arg_1, arg_2):
   empt_lst = []

   for num_1 in arg_1:
      if num_1 not in arg_2:
        empt_lst.append(num_1)


   for num_2 in arg_2:
      if num_2 not in arg_1:
        empt_lst.append(num_2)
   
   return empt_lst

list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]

func_call_2 = difference(list1, list2)
print(func_call_2)