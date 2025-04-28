def find_window_sum(k):
    windows = []
    start = 1
    end = 1
    window_sum = 1

    while start <= k // 2 + 1:
        if window_sum < k:
            end += 1
            window_sum += end
        elif window_sum > k:
            window_sum -= start
            start += 1
        else:
            windows.append((start, end))
            window_sum -= start
            start += 1
    
    return windows