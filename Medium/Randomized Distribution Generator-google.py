import numpy as np

def generate_uniform_draws(num_draws: int) -> list:
    np.random.seed(42)  # Fixed seed for reproducibility
    return np.random.uniform(0, 1, num_draws).tolist()