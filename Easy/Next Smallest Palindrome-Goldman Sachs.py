def next_palindrome(n):
    """
    :type n: int
    :rtype: int
    """
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            return n