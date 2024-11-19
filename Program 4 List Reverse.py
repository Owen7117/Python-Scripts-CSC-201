# Owen O'Neil
# Program 4: List Reverse
# 10/25/24
# This code reverses a list using a recursive statement

# input list
original_list = list(range(1,36))
print(original_list)  # print the original list
list_len = len(original_list)  # get the length of the list

# reverse subroutine
def reverse(lst,s,e,list_len):
    # if the length of the list is <= 2, return the reversed list
    if list_len <= 2:
        return lst

    # otherwise swap the first and last items in the list
    lst[s], lst[e] = lst[e], lst[s]
    # increment the list so it moves one index closer to the middle
    s += 1  # for the starting index
    e -= 1  # for the end index
    # subtract the list length by the number of indexes swapped(2)
    list_len -= 2
    return reverse(lst, s, e, list_len)  # call the recursive statement passing in the list with the changes

# call the subroutine passing in the original list, initialize the first indexes that will be swapped, and the lenght of the list
reverse(original_list, 0, -1, list_len)
# print the output
print(original_list)





