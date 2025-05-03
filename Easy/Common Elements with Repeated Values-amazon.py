def common_elements(input):
    list1 = input["list1"]
    list2 = input["list2"]

    counter1 = {}
    counter2 = {}
    
    for item in list1:
        if item in counter1:
            counter1[item] += 1
        else:
            counter1[item] = 1
    
    for item in list2:
        if item in counter2:
            counter2[item] += 1
        else:
            counter2[item] = 1
    
    common = {}
    for key in counter1:
        if key in counter2:
            common[key] = min(counter1[key], counter2[key])
    
    result = []
    for key, count in common.items():
        result.extend([key] * count)
    
    return result