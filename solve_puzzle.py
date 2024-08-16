def bubble_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            steps.append(arr[:])  # Salin array saat ini
    return steps

if __name__ == "__main__":
    from generate_puzzle.py import generate_puzzle

    puzzle = generate_puzzle()
    print("Generated puzzle:", puzzle)

    solution_steps = bubble_sort(puzzle)
    print("Solution steps:")
    for step in solution_steps:
        print(step)
