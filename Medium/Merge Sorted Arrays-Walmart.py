def merge_sorted_arrays(input):
    arr1 = input[0]
    arr2 = input[1]
    
    merged_array = []
    i = 0  # Index for arr1
    j = 0  # Index for arr2

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # Append the remaining elements of arr1, if any
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    # Append the remaining elements of arr2, if any
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array