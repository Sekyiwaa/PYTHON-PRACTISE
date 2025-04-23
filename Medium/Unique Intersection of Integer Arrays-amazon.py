def find_intersection(input):
    arr1 = input["arr1"]
    arr2 = input["arr2"]
    
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1.intersection(set2))