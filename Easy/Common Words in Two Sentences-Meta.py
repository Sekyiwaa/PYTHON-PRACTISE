import string

def find_common_words(input):
    # Extract sentences
    sentence1 = input[0]
    sentence2 = input[1]

    # Function to clean and split words
    def clean_and_split(sentence):
        return set(word.strip(string.punctuation).lower() for word in sentence.split())

    # Clean and split words from both sentences
    words1 = clean_and_split(sentence1)
    words2 = clean_and_split(sentence2)

    # Find common words and return them sorted
    common_words = words1.intersection(words2)
    return sorted(list(common_words))  # Returns a sorted list of common words