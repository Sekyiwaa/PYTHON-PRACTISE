def modify_array(arr):
    arr.sort()
    left, right = 0, len(arr) - 1
    result = []

    while left <= right:
        result.append(arr[left])
        left += 1
        if left <= right:
            result.append(arr[right])
            right -= 1

    return result