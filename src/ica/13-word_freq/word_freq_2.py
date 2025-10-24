import string

def compute_freq(filename):
    # Step 1: Open and read entire file
    text_file = open(filename, 'r')
    text = text_file.read()   # read the whole file, not just one line
    text_file.close()

    # Step 2: Split into words and remove punctuation
    words = text.split()
    cleaned_words = []        # list to store cleaned words

    for word in words:
        newWord = word.strip(string.punctuation)
        cleaned_words.append(newWord)

    # Test output for Step 2:
    print("Cleaned words list:\n", cleaned_words[:20])  # print first 20 words just to check

    # Step 3.1: Loop over cleaned words independently and print them
    print("\nNow printing each cleaned word:")
    for word in cleaned_words:
        print(word)

# Test with sample file
compute_freq("../TextFiles/alice.txt")
