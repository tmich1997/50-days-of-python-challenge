# Day 48: Binary Search

def search_binary(arg_list, arg_item):
    # sorting the list
    sort_list = sorted(arg_list)

    # settting two variables to track current segment of the list
    # left is index 0, and right is len(list) - 1
    left, right = 0, len(sort_list) - 1

    # WHILE loop for the search iteration
    # when left > right then the entire list has been searched
    while left <= right:

        # calcualting the mid index of the current list
        # its an integer division so no decimials
        mid = (left + right) // 2

        # if the target is found
        # if the index of the item is found, then return the middle index of said item
        if sort_list[mid] == arg_item:
            return mid
        
        # if not found and the target is greater than the mid item
        # it means it will be in the right half
        # so add 1 to the left
        elif sort_list[mid] < arg_item:
            left = mid + 1
        
        # same thing is targte is smaller than the mid item
        # it means that it will be in the left half
        # subtract 1 to the right
        else:
            right = mid - 1
    
    # end loop when no target
    return -1

list_1 = [12, 34, 56, 78, 98, 22, 45, 13]

print(search_binary(list_1, 22))



