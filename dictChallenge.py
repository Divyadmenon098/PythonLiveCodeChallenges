def count_words(input_str):
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
print(word_counts)
