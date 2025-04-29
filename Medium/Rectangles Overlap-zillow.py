def check_overlap(input):
    rect1 = input["rect1"]
    rect2 = input["rect2"]
    
    x1, y1, x2, y2 = sorted(rect1[0:2] + rect1[2:4])
    x3, y3, x4, y4 = sorted(rect2[0:2] + rect2[2:4])

    if x1 > x4 or x2 < x3:
        return False
    if y1 > y4 or y2 < y3:
        return False

    return True