def find_intervals(input):
    """
    Returns up to n smallest consecutive intervals that sum to target_sum.
    - input: dict with keys "nums", "target_sum", "n"
    """
    nums = input["nums"]
    target_sum = input["target_sum"]
    n = input["n"]
    intervals = []

    # Step 1 & 2: gather ALL intervals whose sum == target_sum
    for i in range(len(nums)):
        interval_sum = 0
        for j in range(i, len(nums)):
            interval_sum += nums[j]
            if interval_sum == target_sum:
                # Add the subarray from i to j
                intervals.append(nums[i:j+1])

            # Note: do NOT break on interval_sum > target_sum,
            # because negative numbers might bring it back down.

    # Step 3 & 4: sort intervals by ascending length
    intervals.sort(key=len)

    # Step 5: return up to the first n intervals
    return intervals[:n]