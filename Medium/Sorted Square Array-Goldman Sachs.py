def sorted_squares(arr):
    arr.sort()  
    n = len(arr)
    result = [0] * n
    left, right = 0, n - 1
    i = n - 1

    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result[i] = arr[left] * arr[left]
            left += 1
        else:
            result[i] = arr[right] * arr[right]
            right -= 1
        i -= 1

    return result