def reverse_letters(input_string):
    words = input_string.split()
    reversed_words = [word[::-1] for word in words]
    output_string = ' '.join(reversed_words)
    return output_string