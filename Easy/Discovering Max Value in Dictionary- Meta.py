def find_max_value(dictionary):
    """ 
    :type dictionary: dict
    :rtype: tuple
    """
    max_value = max(dictionary.values())
    max_key = max(dictionary, key = dictionary.get)
    max_index = list(dictionary.keys()).index(max_key)
    return max_value, max_key, max_index
