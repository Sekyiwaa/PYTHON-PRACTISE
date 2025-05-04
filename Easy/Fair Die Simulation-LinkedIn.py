import random
from typing import List

def roll_die(n: int) -> List[int]:
    random.seed(42)
    return [random.randint(1, 6) for _ in range(n)]