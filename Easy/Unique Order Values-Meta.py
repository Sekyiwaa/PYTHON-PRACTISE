def non_duplicate(input):
    """ 
    :type input: List[int]
    :rtype: List[int]
    """
    seen = set()
    seen_add = seen.add
    return [x for x in input if not (x in seen or seen_add(x))]