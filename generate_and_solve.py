import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from generate_puzzle import generate_puzzle
from solve_puzzle import merge_sort
from animate_sorting import animate_sorting

if __name__ == "__main__":
    # Mengukur waktu mulai
    start_time = time.time()

    # Menggenerate teka-teki
    puzzle = generate_puzzle(length=100)  # Menghasilkan 25.000 elemen
    print("Generated puzzle:", puzzle)

    # Menyelesaikan teka-teki menggunakan Merge Sort
    steps = []
    merge_sort(puzzle, 0, len(puzzle) - 1, steps)
    print("Sorting steps recorded.")

    # Membuat animasi penyortiran
    animate_sorting(steps)

    # Mengukur waktu selesai
    end_time = time.time()

    # Menghitung total waktu yang dibutuhkan
    elapsed_time = end_time - start_time
    print(f"Total time taken: {elapsed_time:.2f} seconds")

    # Menyimpan informasi waktu ke dalam README.md
    with open("README.md", "a") as readme_file:
        readme_file.write(f"\n## Performance\n")
        readme_file.write(f"- Time taken to generate, sort, and animate 25,000 elements: {elapsed_time:.2f} seconds\n")
