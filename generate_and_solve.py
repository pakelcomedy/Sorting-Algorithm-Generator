from solve_puzzle import merge_sort  # Mengimpor merge_sort
from generate_puzzle import generate_puzzle
from animate_sorting import animate_sorting

if __name__ == "__main__":
    # Menggenerate teka-teki
    puzzle = generate_puzzle(length=100)  # Menghasilkan 25.000 elemen
    print("Generated puzzle:", puzzle)

    # Menyelesaikan teka-teki menggunakan Merge Sort
    steps = []
    merge_sort(puzzle, 0, len(puzzle) - 1, steps)
    print("Sorting steps recorded.")

    # Membuat animasi penyortiran
    animate_sorting(steps)
    print("Sorting animation created as 'sorting_animation.gif'.")
