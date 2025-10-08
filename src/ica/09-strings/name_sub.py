def count_words(word, text):
    words = text.split()
    return words.count(word)
sentence = count_words("milk", "we get milk from milking a cow")
print(sentence)