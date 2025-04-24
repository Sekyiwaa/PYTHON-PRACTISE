def equal_frequency(nums):
    freq = {}
    # Calculate frequency of each number
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    max_freq = max(freq.values())
    
    additions = {}
    # For each unique number, calculate how many additions are needed
    for num, count in freq.items():
        if count < max_freq:
            additions[num] = max_freq - count

    return additions