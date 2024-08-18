import random

def generate_puzzle(length=100):
    """Generate a list of random integers."""
    return [random.randint(1, 100) for _ in range(length)]
