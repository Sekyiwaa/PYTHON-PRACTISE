import random

random.seed(0)

def die_side(input):
    sides = input["sides"]
    probs = input["probs"]
    rolls = input["rolls"]
    
    results = random.choices(sides, probs, k=rolls)
    
    return results