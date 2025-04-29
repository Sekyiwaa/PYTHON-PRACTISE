def shift_zeroes(arr):
    count = 0  # variable to keep track of non-zero elements
    
    # Traverse the array and move non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    
    # Fill the remaining elements with zeroes
    while count < len(arr):
        arr[count] = 0
        count += 1
    
    return arr