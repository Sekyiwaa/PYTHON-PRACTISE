def find_consecutive_sum(input):
    numbers = input["numbers"]
    target_sum = input["target_sum"]
    n = input["n"]
    
    result = []
    current_sum = sum(numbers[:n])
    if current_sum == target_sum:
        result.append(numbers[:n])
    
    for i in range(n, len(numbers)):
        current_sum += numbers[i] - numbers[i-n]
        if current_sum == target_sum:
            result.append(numbers[i-n+1:i+1])
    
    return result