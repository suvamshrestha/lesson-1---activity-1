def match_words(word_list) :
    count = 0
    for word in word_list:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count
words = ['hello', 'level', 'noon', 'abc', 'xyz', 'python', 'aa']
result = match_words(words)
print(f"Number of words that start and end with the same letter: {result}")        