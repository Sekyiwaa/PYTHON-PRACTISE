def calculate_sum(N):
    total_sum = 0
    for i in range(N + 1):
        if i % 3 != 0 and i % 7 != 0:
            total_sum += i
    return total_sum