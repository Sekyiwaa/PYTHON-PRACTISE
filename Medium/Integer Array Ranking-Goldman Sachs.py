def get_ranks(arr):
    sorted_arr = sorted(set(arr))
    rank_dict = {num: rank for rank, num in enumerate(sorted_arr, start=1)}
    ranks = [rank_dict[num] for num in arr]
    return ranks