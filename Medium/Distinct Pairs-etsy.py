def find_pairs(input):
    k = input["k"]
    arr = input["arr"]

    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1

    result = set()

    for num in arr:
        if num + k in count and (num, num + k) not in result and (num + k, num) not in result:
            result.add((num, num + k))
        if num - k in count and (num, num - k) not in result and (num - k, num) not in result:
            result.add((num-k, num))

    return sorted(list(result), key=lambda x: x[0])