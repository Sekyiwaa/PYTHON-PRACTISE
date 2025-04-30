import random

random.seed(0)

def sample_multimodal(input):
    N = input["n"]
    K = input["keys"]
    W = input["weights"]
    
    # Sample N elements based on the weights W
    sampled_elements = random.choices(K, weights=W, k=N)
    
    return sampled_elements