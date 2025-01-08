def biased_coin_flip(input):
    p = input["probability"]
    N = input["N"]
    outcomes = [0, 1]
    probabilities = [p, 1 - p]
    
    results = random.choices(outcomes, probabilities, k=N)
    
    return results