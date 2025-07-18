#level
#eve
#v
# A string is a palindrome if the first character is the same as the last character and the rest of the string is a palindrome -recursive step
def is_palindrome(a):
  if len(a) <= 1:
    return True
  return a[0] == a[-1] and is_palindrome(a[1:-1])


