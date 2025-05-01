def key_of_highest_value(dct):
    max_val = max(dct.values())
    max_keys = [k for k, v in dct.items() if v == max_val]
    return min(max_keys)