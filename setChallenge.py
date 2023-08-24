def combine_list(list1, list2):
    list_one_to_set = set(list1)
    list_two_to_set = set(list2)
    master_list = list_one_to_set.intersection(list_two_to_set)
    return master_list


first = [1, 2, 3, 3, 4]
second = [4, 3, 5, 5, 5, 6]
print(combine_list(first, second))
