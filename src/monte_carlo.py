import random
from typing import List

def simulate_crashes(days: int, probability: float = 0.045) -> List[int]:
    return [1 if random.random() < probability else 0 for _ in range(days)]
