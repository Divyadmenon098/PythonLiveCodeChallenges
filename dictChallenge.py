#Tried using defaultdict:
"""Defaultdict automatically sets missing word counts to 0, so we dont have to check if a word exists before incrementing. Comparing the two codes the one with 
defaultdict takes less execution time but slightly takes more memory space as will automatically create a new entry and initialize the value to the default i.e. 0 here.""" 

from collections import defaultdict
def count_words(input_str):
    word_count = defaultdict(int)
    for word in input_str.lower().split():
        word_count[word] += 1
    return dict(word_count)
input_string = "This is a sample string. This string is just an example."
print(count_words(input_string))

#Source code
"""def count_words(input_str):
    word_count = {}
    words = input_str.lower().split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


input_string = "This is a sample string. This string is just an example."
word_counts = count_words(input_string)
print(word_counts)"""


