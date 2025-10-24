import string

def compute_freq(filename):
    text_file = open(filename, 'r')
    text = text_file.read()
    print(text)
    words = text.split()
    cleaned_text = []
    for word in words:
        newWord = word.strip(string.punctuation)
        cleaned_text.append(newWord)

    print(cleaned_text)

    freq = {}
    for word in cleaned_text:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return(freq)

compute_freq("../TextFiles/alice.txt")
