def binary_search(arr, target):
    left = 0
    right= len(arr) - 1

while (left <= right):
    mid = (left + right) // 2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

return -1