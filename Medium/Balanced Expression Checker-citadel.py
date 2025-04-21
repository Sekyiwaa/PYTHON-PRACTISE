def is_balanced(expression):
    stack = []
    opening_brackets = ['(', '[', '{', '<']
    closing_brackets = [')', ']', '}', '>']
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(char):
                return False
    
    return len(stack) == 0