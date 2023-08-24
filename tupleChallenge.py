def sort_list(list_of_tuple):

    finished_sort = sorted(list_of_tuple, key=lambda srt: srt[-1])
    return finished_sort


list_of_ = [(2, 3), (6, 1), (7, 2)]
print(sort_list(list_of_))
