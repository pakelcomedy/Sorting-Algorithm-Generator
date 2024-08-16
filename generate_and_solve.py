from generate_puzzle import generate_puzzle
from solve_puzzle import bubble_sort
from animate_sorting import animate_sorting

if __name__ == "__main__":
    # Menggenerate teka-teki
    puzzle = generate_puzzle()
    print("Generated puzzle:", puzzle)

    # Menyelesaikan teka-teki
    solution_steps = bubble_sort(puzzle)
    print("Sorting steps recorded.")

    # Membuat animasi penyortiran
    animate_sorting(solution_steps)
    print("Sorting animation created as 'sorting_animation.gif'.")
