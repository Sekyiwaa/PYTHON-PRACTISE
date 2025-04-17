def count_additional_chars(text):
    chars = set(text)
    digits = set([c for c in text if c.isdigit()])
    additional_chars = 0
    
    for char in chars:
        if char.isalpha():
            digit = char_to_digit(char)
            if digit not in digits:
                additional_chars += 1
        elif char.isdigit():
            letter = digit_to_letter(char)
            if letter not in chars:
                additional_chars += 1
    
    return additional_chars

def char_to_digit(char):
    return str(ord(char.lower()) - ord('a'))

def digit_to_letter(digit):
    return chr(ord('a') + int(digit))