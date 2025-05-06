def max_subarray_sum(arr):
    if not arr:
        return 0, -1, -1
    
    max_sum = current_sum = arr[0]
    start = end = s = 0
    
    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            s = i
        else:
            current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i
    
    return max_sum, start, end