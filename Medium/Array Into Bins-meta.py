def histogram(input):
    array = input["array"]
    N = input["N"]
    
    min_value = min(array)
    max_value = max(array)
    bin_width = (max_value - min_value) / N
    
    bins = [0] * N
    
    for num in array:
        bin_index = int((num - min_value) // bin_width)
        if bin_index == N:
            bin_index -= 1
        bins[bin_index] += 1
    
    return bins