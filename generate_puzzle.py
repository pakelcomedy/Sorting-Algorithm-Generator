import random

def generate_puzzle(length=500, min_value=1, max_value=100):
    """Generate a random list of integers."""
    return [random.randint(min_value, max_value) for _ in range(length)]

if __name__ == "__main__":
    puzzle = generate_puzzle()
    print("Generated puzzle:", puzzle)
