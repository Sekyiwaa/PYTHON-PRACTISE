def count_words(sentences):
    word_count = {}
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count