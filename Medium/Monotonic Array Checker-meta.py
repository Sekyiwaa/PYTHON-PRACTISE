def is_monotonic(lst):
    if len(lst) < 2:
        return True
    is_increasing = is_decreasing = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            is_increasing = False
        if lst[i] < lst[i+1]:
            is_decreasing = False
    return is_increasing or is_decreasing