import numpy as np

def generate_and_normalize_matrix(input):
    rows = input[0]
    cols = input[1]
    p = 0.5  # Probability for Bernoulli trials
    divisor = 3  # Normalization factor

    np.random.seed(42)  # Ensures reproducibility
    matrix = np.random.binomial(1, p, size=(rows, cols)).tolist()  # Generates a binary matrix

    # Normalize the matrix
    normalized_matrix = [[x / divisor for x in row] for row in matrix]

    return normalized_matrix