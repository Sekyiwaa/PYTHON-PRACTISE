def sum_digits(numbers):
    """ 
    :type numbers: List[int]
    :rtype: List[int]
    """
    result =[]
    for num in numbers:
        digit_sum =sum(int(digit) for digit in str(abs(num)))
        result.append(digit_sum)
    return result