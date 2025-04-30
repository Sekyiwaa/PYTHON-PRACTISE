def count_ways(n):
    if n <= 1:
        return 1
    else:
        return count_ways(n-1) + count_ways(n-2)